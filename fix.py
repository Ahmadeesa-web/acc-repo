import re

with open(r'd:\web.py\backend\app\routers\finance.py', 'r') as f:
    text = f.read()

# Fix the PaymentStatus imports and usage
text = re.sub(
    r'from \.\.models\.finance import LedgerEntryType\nfrom \.\.models\.sale import Sale, SaleItem\nfrom \.\.models\.purchase import Purchase, PurchaseItem',
    r'from ..models.finance import LedgerEntryType\nfrom ..models.sale import Sale, SaleItem, PaymentStatus as SalePaymentStatus\nfrom ..models.purchase import Purchase, PurchaseItem, PaymentStatus as PurchasePaymentStatus',
    text
)
text = text.replace('s.payment_status = "PAID"', 's.payment_status = SalePaymentStatus.PAID')
text = text.replace('s.payment_status = "PARTIAL"', 's.payment_status = SalePaymentStatus.PARTIAL')
text = text.replace('p.payment_status = "PAID"', 'p.payment_status = PurchasePaymentStatus.PAID')
text = text.replace('p.payment_status = "PARTIAL"', 'p.payment_status = PurchasePaymentStatus.PARTIAL')

# Fix current_user bug in owners-equity
text = text.replace('bs_prev = get_balance_sheet(as_of=prev_date, db=db, _=current_user)', 'bs_prev = get_balance_sheet(as_of=prev_date, db=db, _=_)')
text = text.replace('pl = profit_loss_report(from_date=from_date, to_date=to_date, db=db, _=current_user)', 'pl = profit_loss_report(from_date=from_date, to_date=to_date, db=db, _=_)')

# Fix trailing slashes in @router decorators
text = re.sub(r'@router\.(get|post|put|delete)\(\"([^\"]+?)(?<!/)\"', r'@router.\1("\2/"', text)

with open(r'd:\web.py\backend\app\routers\finance.py', 'w') as f:
    f.write(text)
