import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class TxInfoModel(Model):
  tx_id  = columns.UUID(primary_key=true, default=uuid.uuid4)
  Time = columns.Integer(index=True)
  V1  = columns.Float()
  V2  = columns.Float()
  V3  = columns.Float()
  V4  = columns.Float()
  V5  = columns.Float()
  V6  = columns.Float()
  V7  = columns.Float()
  V8  = columns.Float()
  V9  = columns.Float()
  V10 = columns.Float()
  V11 = columns.Float()
  V12 = columns.Float()
  V13 = columns.Float()
  V14 = columns.Float()
  V15 = columns.Float()
  V16 = columns.Float()
  V17 = columns.Float()
  V18 = columns.Float()
  V19 = columns.Float()
  V20 = columns.Float()
  V22 = columns.Float()
  V23 = columns.Float()
  V24 = columns.Float()
  V25 = columns.Float()
  V26 = columns.Float()
  V27 = columns.Float()
  V28 = columns.Float()
  Amount = columns.Float(required=False)
  C  =columns.Integer(index=True)
  
  
  
  
  
