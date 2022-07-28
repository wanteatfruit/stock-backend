from django.db import models
from django.forms import NullBooleanField
from sqlalchemy import true

class AAPL(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)
    Positive = models.FloatField(null=true)
    Negative = models.FloatField(null=true)

class ABBV(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class ABI(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class ALV(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class AMGN(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class AMZN(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)
    Positive = models.FloatField(null=true)
    Negative = models.FloatField(null=true)

class BATS(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class BA(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class BHP(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class BP(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class CSCO(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class CVX(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class C(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class DD(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class DIS(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class GE(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class GOOG(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)
    Positive = models.FloatField(null=true)
    Negative = models.FloatField(null=true)

class GSK(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class HSBA(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class IBM(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)
    Positive = models.FloatField(null=true)
    Negative = models.FloatField(null=true)

class INTC(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class JNJ(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class JPM(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class KO(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class MA(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class MCD(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class META(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class MMM(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class MRK(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class MSFT(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)
    Positive = models.FloatField(null=true)
    Negative = models.FloatField(null=true)

class NESN(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class NOVN(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class NVDA(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)
    Positive = models.FloatField(null=true)
    Negative = models.FloatField(null=true)

class ORCL(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class PEP(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class PFE(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class PG(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class PM(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class ROG(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class RY(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class SAN(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class SHEL(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class SIE(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class SMSN(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class TM(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class TSM(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class TTE(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class V(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class WMT(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)

class XOM(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Adj_Close = models.FloatField(null=true)
    Predicted = models.FloatField(null=true)
    




    
class PFYH_600000(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class MSYH_600016(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class BGGF_600019(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGSH_600028(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class NFHK_600029(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZXZQ_600030(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class SYZG_600031(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZSYH_600036(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class BLFZ_600048(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGLT_600050(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class SQJT_600104(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class FXYY_600196(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class HRYY_600276(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class WHHX_600309(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class HXXF_600340(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class GZMT_600519(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class HLSN_600585(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class HEZJ_600690(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class SAGD_600703(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class HTZQ_600837(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class YLGF_600887(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZXJT_601066(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGSH_601088(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGGH_601111(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class GYFL_601138(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class XYYH_601166(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGTJ_601186(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class GTJA_601211(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class SHYH_601229(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class NYYH_601288(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGPA_601318(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGRB_601319(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class JTYH_601328(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class XHBX_601336(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGZT_601390(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class GSYH_601398(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGTB_601601(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGRS_601628(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGJZ_601668(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class HTZQ_601688(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGZC_601766(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGJJ_601800(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class GDYH_601818(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGSY_601857(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGGL_601888(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class JSYH_601939(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGYH_601988(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class ZGZG_601989(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class YMKD_603259(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)

class LYMY_603993(models.Model):
    Date = models.CharField(max_length=10, primary_key=true)
    Open = models.FloatField(null=true)
    Close = models.FloatField(null=true)
    High = models.FloatField(null=true)
    Low = models.FloatField(null=true)
    Volume = models.FloatField(null=true)
    Code = models.IntegerField(null=true)
    Predicted = models.FloatField(null=true)