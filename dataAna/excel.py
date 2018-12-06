import xlrd
import sys

print(sys.getdefaultencoding())
wordbook = xlrd.open_workbook('/Users/wangqun/BasedPython/dataAna/DEAL_DETAIL.xls')

print(wordbook.sheet_names())
sheet = wordbook.sheet_by_index(1)

