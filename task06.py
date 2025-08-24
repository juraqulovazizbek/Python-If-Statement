nomer = input("raqamingizni kiriting: ")  # Masalan: 991234455
kod = nomer[:2]

if kod in ("90", "91"):
    print("Ucell")

if kod in ("93", "94"):
    print("Beeline")

if kod in ("95", "97"):
    print("Uzmobile")

if kod not in ("90", "91", "93", "94", "95", "97"):
    print("Operator topilmadi")
