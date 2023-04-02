import os
import time

import click
import inquirer
import pinyin
from appdirs import *
from prettytable import PrettyTable

from .utils import net_api
from .utils import config

config_path = os.path.join(user_config_dir(), 'config.json')
config_parser = config.Config(config_path)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--interval', default=5, help='refresh interval of stock value.')
@click.option('--fish', is_flag=True, help='catch fish when you work.')
def fly(interval, fish):
    watch_list = config_parser.get_watch_list()
    code_list = list(map(lambda s: s['QuoteID'], watch_list))

    if len(code_list) == 0:
        print("There are no stock in watch list, please add first!")
        return

    pre_table = ''
    while True:
        stocks = net_api.get_bullets_value(code_list)

        # 格式化打印
        x = PrettyTable(['name', 'code', 'price', 'percent'])
        x.align = 'r'
        for stock in stocks:
            name = stock['f14']
            code = stock['f12']
            pre_price = stock['f18']
            price = stock['f2']
            percent = (price - pre_price) / pre_price * 100

            if fish:
                x.add_row([pinyin.get(name, format="strip"), code, price / 100, f'{percent:.2f}%'])
            else:
                if percent < 0:
                    x.add_row([name, code, price / 100, f'\033[32m{percent:.2f}%\033[0m'])
                else:
                    x.add_row([name, code, price / 100, f'\033[31m{percent:.2f}%\033[0m'])

        br_count = pre_table.count('\n', 0, len(pre_table))

        x_table = str(x)
        magic_char = '\033[F'
        print(f'{magic_char * br_count}{x_table}', end="")

        pre_table = x_table
        time.sleep(interval)


@cli.command()
def remove():
    """Remove stock from watch list, such as `bullet remove`."""

    stocks = config_parser.get_watch_list()

    if len(stocks) == 0:
        print("You don't have any stock in watch list")

    # dic(stock_name to stock)
    stocks_map = {}
    for stock in stocks:
        stock_name = stock['Name']
        stock_code = stock['Code']
        stocks_map[f'{stock_name}({stock_code})'] = stock

    # ask user for stock
    questions = [
        inquirer.List('select_stock',
                      message="Which stock do you want to remove?",
                      choices=stocks_map.keys(),
                      carousel=True,
                      ),
    ]
    answers = inquirer.prompt(questions)
    select_stock_name = answers['select_stock']
    select_stock = stocks_map[select_stock_name]

    # remove stock from watch list
    config_parser.remove_stock_from_watch_list(select_stock)


@cli.command()
@click.argument('name')
def add(name):
    """Add stock to watch list, such as `bullet add 茅台`."""

    # search stock
    stocks = net_api.search_bullets(name)

    # dic(stock_name to stock)
    stocks_map = {}
    for stock in stocks:
        stock_name = stock['Name']
        stock_code = stock['Code']
        stocks_map[f'{stock_name}({stock_code})'] = stock

    # ask user for stock
    questions = [
        inquirer.List('select_stock',
                      message="Which stock do you need?",
                      choices=stocks_map.keys(),
                      carousel=True,
                      ),
    ]
    answers = inquirer.prompt(questions)
    select_stock_name = answers['select_stock']
    select_stock = stocks_map[select_stock_name]

    # add stock to watch list
    config_parser.add_stock_to_watch_list(select_stock)
