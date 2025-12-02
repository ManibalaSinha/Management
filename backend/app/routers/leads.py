from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models
from ..database import get_db
from ..services.fraud_service import evaluate_lead

router = APIRouter()
@router.post('/', response_model=schemas.LeadOut)
def create_lead(payload: schemas.LeadCreate, db: Session = Depends(get_db)):
# simple evaluate
   data = payload.dict()
   score = evaluate_lead(data)
   status = 'flagged' if score >= 50 else 'new'
   lead = models.Lead(name=data['name'], email=data['email'],
   postal_code=data.get('postal_code'), risk_score=score, status=status)
   db.add(lead); db.commit(); db.refresh(lead)
   return lead
@router.get('/', response_model=List[schemas.LeadOut])
def list_leads(q: str = Query('', alias='q'), postal: str = Query(None), status:
   str = Query(None), limit: int = 20, offset: int = 0, db: Session = Depends(get_db)):
   query = db.query(models.Lead)
   if q:
      query = query.filter((models.Lead.name.ilike(f'%{q}%')) |
(models.Lead.email.ilike(f'%{q}%')))
   if postal:
      query = query.filter(models.Lead.postal_code == postal)
   if status:
      query = query.filter(models.Lead.status == status)
   results =query.order_by(models.Lead.created_at.desc()).limit(limit).offset(offset).all()
   return results
@router.get('/{lead_id}', response_model=schemas.LeadOut)
def get_lead(lead_id: int, db: Session = Depends(get_db)):
   lead = db.query(models.Lead).filter(models.Lead.id == lead_id).first()
   if not lead:
      raise HTTPException(status_code=404, detail='Not found')
   return lead