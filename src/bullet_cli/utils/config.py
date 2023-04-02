import py_json_config


class Config(py_json_config.JSONConfig):
    def get_watch_list(self):
        return self.get_value('watch_list')

    def add_stock_to_watch_list(self, stock):
        watch_list = self.get_watch_list()
        stock_code = stock['Code']
        stock_name = stock['Name']
        stock_id = f'{stock_name}({stock_code})'

        if stock_code not in map(lambda x: x['Code'], watch_list):
            watch_list.append(stock)
            self.set_value('watch_list', watch_list)
            print(f'add {stock_id} successfully!')
        else:
            print(f'{stock_id} already exists!')

    def remove_stock_from_watch_list(self, stock):
        watch_list = self.get_watch_list()
        stock_code = stock['Code']
        stock_name = stock['Name']
        stock_id = f'{stock_name}({stock_code})'

        if stock_code not in map(lambda x: x['Code'], watch_list):
            print(f'{stock_id} not in watch list!')
        else:
            watch_list.remove(stock)
            self.set_value('watch_list', watch_list)
            print(f'remove {stock_id} successfully!')
