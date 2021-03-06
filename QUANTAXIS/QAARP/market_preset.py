#
import pandas as pd
from functools import lru_cache
class MARKET_PRESET:

    def __init__(self):
        """
              unit_table 合约乘数
              commission_coeff_peramount 按总量计算手续费系数
              commission_coeff_pervol 按手数计算的手续费系数
              commission_coeff_today_peramount 按总量计算的平今手续费系数
              commission_coeff_today_pervol 按手数计算的平今手续费系数

              多头开仓保证金系数
              空头开仓保证金系数
              """

        self.table = {
            'P': {
                'buy_frozen_coeff': 0.06,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 2.5,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 1.25,
                'exchange': 'DCE',
                'name': '棕榈油',
                'sell_frozen_coeff': 0.06,
                'unit_table': 10
            },
            'Y': {
                'buy_frozen_coeff': 0.06,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 2.5,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 1.25,
                'exchange': 'DCE',
                'name': '豆油',
                'sell_frozen_coeff': 0.06,
                'unit_table': 10
            },
            'M': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 1.5,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 0.75,
                'exchange': 'DCE',
                'name': '豆粕',
                'sell_frozen_coeff': 0.07,
                'unit_table': 10
            },
            'A': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 2.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 2.0,
                'exchange': 'DCE',
                'name': '豆一',
                'sell_frozen_coeff': 0.07,
                'unit_table': 10
            },
            'B': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 1.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 1.0,
                'exchange': 'DCE',
                'name': '豆二',
                'sell_frozen_coeff': 0.07,
                'unit_table': 10
            },
            'C': {
                'buy_frozen_coeff': 0.05,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 1.2,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 0.6,
                'exchange': 'DCE',
                'name': '玉米',
                'sell_frozen_coeff': 0.05,
                'unit_table': 10
            },
            'L': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 2.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 1.0,
                'exchange': 'DCE',
                'name': '塑料',
                'sell_frozen_coeff': 0.07,
                'unit_table': 5
            },
            'JD': {
                'buy_frozen_coeff': 0.08,
                'commission_coeff_peramount': 0.00015,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 0.00015,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'DCE',
                'name': '鸡蛋',
                'sell_frozen_coeff': 0.08,
                'unit_table': 10
            },
            'J': {
                'buy_frozen_coeff': 0.09,
                'commission_coeff_peramount': 6e-05,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 0.00018,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'DCE',
                'name': '焦炭',
                'sell_frozen_coeff': 0.09,
                'unit_table': 100
            },
            'JM': {
                'buy_frozen_coeff': 0.09,
                'commission_coeff_peramount': 6e-05,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 0.00018,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'DCE',
                'name': '焦煤',
                'sell_frozen_coeff': 0.09,
                'unit_table': 60
            },
            'FB': {
                'buy_frozen_coeff': 0.2,
                'commission_coeff_peramount': 0.0001,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 5e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'DCE',
                'name': '纤维板',
                'sell_frozen_coeff': 0.2,
                'unit_table': 500
            },
            'I': {
                'buy_frozen_coeff': 0.08,
                'commission_coeff_peramount': 6e-05,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 6e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'DCE',
                'name': '铁矿石',
                'sell_frozen_coeff': 0.08,
                'unit_table': 100
            },
            'PP': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 6e-05,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 3e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'DCE',
                'name': '聚丙烯',
                'sell_frozen_coeff': 0.07,
                'unit_table': 5
            },
            'EG': {
                'buy_frozen_coeff': 0.06,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 4.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 2.0,
                'exchange': 'DCE',
                'name': '乙二醇',
                'sell_frozen_coeff': 0.06,
                'unit_table': 10
            },
            'BB': {
                'buy_frozen_coeff': 0.2,
                'commission_coeff_peramount': 0.0001,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 5e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'DCE',
                'name': '胶合板',
                'sell_frozen_coeff': 0.2,
                'unit_table': 500
            },
            'V': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 2.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 1.0,
                'exchange': 'DCE',
                'name': 'PVC',
                'sell_frozen_coeff': 0.07,
                'unit_table': 5
            },
            'CS': {
                'buy_frozen_coeff': 0.05,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 1.5,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 0.75,
                'exchange': 'DCE',
                'name': '玉米淀粉',
                'sell_frozen_coeff': 0.05,
                'unit_table': 10
            },
            'AL': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 3.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 3.0,
                'exchange': 'SHFE',
                'name': '沪铝',
                'sell_frozen_coeff': 0.07,
                'unit_table': 5
            },
            'AU': {
                'buy_frozen_coeff': 0.05,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 10.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 10.0,
                'exchange': 'SHFE',
                'name': '沪金',
                'sell_frozen_coeff': 0.05,
                'unit_table': 1000
            },
            'CU': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 5e-05,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 5e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'SHFE',
                'name': '沪铜',
                'sell_frozen_coeff': 0.07,
                'unit_table': 5
            },
            'RU': {
                'buy_frozen_coeff': 0.09,
                'commission_coeff_peramount': 4.5e-05,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 2.25e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'SHFE',
                'name': '橡胶',
                'sell_frozen_coeff': 0.09,
                'unit_table': 10
            },
            'FU': {
                'buy_frozen_coeff': 0.1,
                'commission_coeff_peramount': 5e-05,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 5e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'SHFE',
                'name': '燃油',
                'sell_frozen_coeff': 0.1,
                'unit_table': 10
            },
            'RB': {
                'buy_frozen_coeff': 0.09,
                'commission_coeff_peramount': 0.0001,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 0.0001,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'SHFE',
                'name': '螺纹钢',
                'sell_frozen_coeff': 0.09,
                'unit_table': 10
            },
            'WR': {
                'buy_frozen_coeff': 0.08,
                'commission_coeff_peramount': 4e-05,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 4e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'SHFE',
                'name': '线材',
                'sell_frozen_coeff': 0.08,
                'unit_table': 10
            },
            'ZN': {
                'buy_frozen_coeff': 0.08,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 3.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 3.0,
                'exchange': 'SHFE',
                'name': '沪锌',
                'sell_frozen_coeff': 0.08,
                'unit_table': 5
            },
            'BU': {
                'buy_frozen_coeff': 0.08,
                'commission_coeff_peramount': 0.0001,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 5e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'SHFE',
                'name': '沥青',
                'sell_frozen_coeff': 0.08,
                'unit_table': 10
            },
            'AG': {
                'buy_frozen_coeff': 0.06,
                'commission_coeff_peramount': 5e-05,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 2.5e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'SHFE',
                'name': '沪银',
                'sell_frozen_coeff': 0.06,
                'unit_table': 15
            },
            'SN': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 3.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 3.0,
                'exchange': 'SHFE',
                'name': '沪锡',
                'sell_frozen_coeff': 0.07,
                'unit_table': 1
            },
            'NI': {
                'buy_frozen_coeff': 0.08,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 6.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 3.0,
                'exchange': 'SHFE',
                'name': '沪镍',
                'sell_frozen_coeff': 0.08,
                'unit_table': 1
            },
            'HC': {
                'buy_frozen_coeff': 0.08,
                'commission_coeff_peramount': 0.0001,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 5e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'SHFE',
                'name': '热轧卷板',
                'sell_frozen_coeff': 0.08,
                'unit_table': 10
            },
            'PB': {
                'buy_frozen_coeff': 0.08,
                'commission_coeff_peramount': 4e-05,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 4e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'SHFE',
                'name': '沪铅',
                'sell_frozen_coeff': 0.08,
                'unit_table': 5
            },
            'SP': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 5e-05,
                'commission_coeff_pervol': 0.0,
                'commission_coeff_today_peramount': 5e-05,
                'commission_coeff_today_pervol': 0.0,
                'exchange': 'SHFE',
                'name': '纸浆',
                'sell_frozen_coeff': 0.07,
                'unit_table': 10
            },
            'SC': {
                'buy_frozen_coeff': 0.1,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 20.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 20.0,
                'exchange': 'SHFE',
                'name': '原油',
                'sell_frozen_coeff': 0.1,
                'unit_table': 1000
            },
            'RI': {
                'buy_frozen_coeff': 0.05,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 2.5,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 2.5,
                'exchange': 'ZCE',
                'name': '早籼稻',
                'sell_frozen_coeff': 0.05,
                'unit_table': 20
            },
            'RS': {
                'buy_frozen_coeff': 0.2,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 2.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 2.0,
                'exchange': 'ZCE',
                'name': '菜油',
                'sell_frozen_coeff': 0.2,
                'unit_table': 5
            },
            'SR': {
                'buy_frozen_coeff': 0.05,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 3.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 1.5,
                'exchange': 'ZCE',
                'name': '白糖',
                'sell_frozen_coeff': 0.05,
                'unit_table': 10
            },
            'TA': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 3.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 1.5,
                'exchange': 'ZCE',
                'name': 'PTA',
                'sell_frozen_coeff': 0.07,
                'unit_table': 5
            },
            'WH': {
                'buy_frozen_coeff': 0.2,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 2.5,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 1.25,
                'exchange': 'ZCE',
                'name': '强麦',
                'sell_frozen_coeff': 0.2,
                'unit_table': 10
            },
            'FG': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 3.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 6.0,
                'exchange': 'ZCE',
                'name': '玻璃',
                'sell_frozen_coeff': 0.07,
                'unit_table': 20
            },
            'OI': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 2.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 1.0,
                'exchange': 'ZCE',
                'name': '菜油',
                'sell_frozen_coeff': 0.07,
                'unit_table': 10
            },
            'ZC': {
                'buy_frozen_coeff': 0.08,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 4.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 4.0,
                'exchange': 'ZCE',
                'name': '菜籽',
                'sell_frozen_coeff': 0.08,
                'unit_table': 10
            },
            'CF': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 4.3,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 2.15,
                'exchange': 'ZCE',
                'name': '郑棉',
                'sell_frozen_coeff': 0.07,
                'unit_table': 5
            },
            'RM': {
                'buy_frozen_coeff': 0.06,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 1.5,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 0.75,
                'exchange': 'ZCE',
                'name': '菜粕',
                'sell_frozen_coeff': 0.06,
                'unit_table': 10
            },
            'PM': {
                'buy_frozen_coeff': 0.05,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 5.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 5.0,
                'exchange': 'ZCE',
                'name': '普麦',
                'sell_frozen_coeff': 0.05,
                'unit_table': 10
            },
            'SM': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 3.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 6.0,
                'exchange': 'ZCE',
                'name': '锰硅',
                'sell_frozen_coeff': 0.07,
                'unit_table': 5
            },
            'SF': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 3.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 9.0,
                'exchange': 'ZCE',
                'name': '硅铁',
                'sell_frozen_coeff': 0.07,
                'unit_table': 5
            },
            'LR': {
                'buy_frozen_coeff': 0.05,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 3.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 3.0,
                'exchange': 'ZCE',
                'name': '晚籼稻',
                'sell_frozen_coeff': 0.05,
                'unit_table': 20
            },
            'MA': {
                'buy_frozen_coeff': 0.07,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 2.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 6.0,
                'exchange': 'ZCE',
                'name': '甲醇',
                'sell_frozen_coeff': 0.07,
                'unit_table': 10
            },
            'JR': {
                'buy_frozen_coeff': 0.05,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 3.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 3.0,
                'exchange': 'ZCE',
                'name': '粳稻',
                'sell_frozen_coeff': 0.05,
                'unit_table': 20
            },
            'CY': {
                'buy_frozen_coeff': 0.05,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 4.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 2.0,
                'exchange': 'ZCE',
                'name': '棉纱',
                'sell_frozen_coeff': 0.05,
                'unit_table': 5
            },
            'AP': {
                'buy_frozen_coeff': 0.2,
                'commission_coeff_peramount': 0.0,
                'commission_coeff_pervol': 20.0,
                'commission_coeff_today_peramount': 0.0,
                'commission_coeff_today_pervol': 20.0,
                'exchange': 'ZCE',
                'name': '苹果',
                'sell_frozen_coeff': 0.2,
                'unit_table': 10
            }
        }

    # 手续费比例
    
    @property
    @lru_cache()
    def pdtable(self):
        return pd.DataFrame(self.table)

    def __repr__(self):
        return '< QAMARKET_PRESET >'

    @property
    def code_list(self):
        return list(self.table.keys())

    
    @property
    def exchange_list(self):
        """返回已有的市场列表
        
        Returns:
            [type] -- [description]
        """

        return list(self.pdtable.loc['exchange'].unique())

    
    def get_exchangecode(self, exchange):
        return self.pdtable.T.query('exchange=="{}"'.format(exchange)).index.tolist()

    def get_code(self, code):
        try:
            int(str(code)[1])
            code = code[0]
        except:
            if str(code).endswith('L8') or str(code).endswith('L9'):
                code = code[0:-2]
            else:
                code = code[0:2]
        return self.table.get(str(code).upper())

    # 
    def get_exchange(self, code):
        return self.get_code(code).get('exchange')

    def get_name(self, code):
        return self.get_code(code).get('name')

    def get_commission_coeff(self, code, dtype):
        return self.get_code(code).get('unit_table')

    # 印花税系数
    def get_tax_coeff(self, code, dtype):
        pass

    # 交易时间
    def get_trade_time(self, code, dtype):
        pass

    # 交易杠杆
    def get_unit(self, code):
        return self.get_code(code).get('unit_table')

    #
    def get_frozen(self, code):
        """买卖冻结保证金

              Arguments:
                     code {[type]} -- [description]

              Returns:
                     [type] -- [description]
              """

        return self.get_code(code).get('buy_frozen_coeff')
