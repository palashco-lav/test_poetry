# from src import widget
# from src.widget import get_date
# from src import generators
# from src.generators import card_number_generator, filter_by_currency  # filter_by_currency, transaction_descriptions
from src.utils import get_transaction_data
from src.masks import get_mask_card_number, get_mask_account


get_mask_card_number("0123456789012345")
get_mask_account("0123456789012345")
get_transaction_data("")
