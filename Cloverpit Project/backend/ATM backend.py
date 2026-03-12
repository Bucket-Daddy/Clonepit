#ATM backend script
debtNum = 1
debtMult = 1

InitialDebtAmounts = (75, 200, 666, 2222, 12500, 33333, 66666, 200000, 1000000)
if debtNum < 10:
    debtAmount = InitialDebtAmounts[debtNum - 1] * debtMult
else:
    overLimit = debtNum - 9
    scaleFactor = overLimit ** max(0, overLimit - 3)
    if overLimit > 7:
        overLimit += overLimit - 7
    debtAmount = 1000000 * ((6 * 2 ** (overLimit - 1)) ** overLimit) * scaleFactor * debtMult