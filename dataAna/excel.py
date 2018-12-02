
import xlrd
import sys
#print(sys.version)
#sys.stdout =  codecs.getwriter("utf-8")(sys.stdout.detach())
#sys.stdout.reconfigure(encoding='utf-8')
print(sys.getdefaultencoding())
wordbook = xlrd.open_workbook('/Users/wangqun/BasedPython/dataAna/DEAL_DETAIL.xls')
