sina = int(input("値段（円）"))
zeiritsu = int(input("消費税率（％）"))
print("消費税" + str(round(zeiritsu / 100 * sina)) + "円")