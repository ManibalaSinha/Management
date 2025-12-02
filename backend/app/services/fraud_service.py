# simple rule-based scoring
DISPOSABLE_DOMAINS = {'mailinator.com', 'tempmail.com'}
BANNED_POSTAL_PREFIXES = {'XXX', '000'}
def evaluate_lead(payload: dict, existing_count_same_ip: int = 0):
   score = 0
   email = payload.get('email','')
   if '@' in email:
      domain = email.split('@')[-1]
   if domain in DISPOSABLE_DOMAINS:
      score += 30
   postal = (payload.get('postal_code') or '').upper()
   for p in BANNED_POSTAL_PREFIXES:
      if postal.startswith(p):
         score += 40
      if existing_count_same_ip > 5:
         score += 20
      return score
