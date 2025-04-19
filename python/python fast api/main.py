from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Dasturlash tillari haqida malumot"}


@app.get("/python/")
def read_items(skip: int = 0, limit: int = 10):
    return {"Python — bu yuqori darajadagi, dinamik va oson organiladigan dasturlash tili bolib, 1980-yillarda Guido van Rossum tomonidan ishlab chiqilgan. Python dasturlash tili ishlab chiquvchilarga va foydalanuvchilarga qulay sintaksis, yuqori darajadagi abstraktsiya va koplab kutubxonalar yordamida tez va samarali dasturlar yaratishga imkon beradi."}


@app.get("/HTML/")
def read_items(skip: int = 0, limit: int = 10):
    return {"HTML (HyperText Markup Language) — bu veb-sahifalarni yaratish uchun ishlatiladigan belgilash (markup) tilidir. HTML yordamida matn, rasm, videolar, havolalar va boshqa turli xil elementlar veb-sahifada joylashtiriladi va ko‘rsatiladi. HTML barcha veb-saytlar va veb-ilovalar uchun asosiy struktura bo‘lib xizmat qiladi."}


@app.get("/java/")
def read_items(skip: int = 0, limit: int = 10):
    return {"Java — bu yuqori darajadagi obyektga yo'naltirilgan dasturlash tili bo'lib, u 1990-yillarda Sun Microsystems (hozirda Oracle) tomonidan ishlab chiqilgan. Java, bugungi kunda eng mashhur va keng tarqalgan dasturlash tillaridan biri bo'lib, uning asosiy afzalliklaridan biri — platformalardan mustaqil ishlash imkoniyatidir. Java kodingizni bir marta yozib, turli platformalarda (Windows, Linux, MacOS) ishlatishingiz mumkin. Bu Write Once, Run Anywhere (WORA) degan kontseptsiyani taqdim etadi."}




@app.get("/c++/")
def read_items(skip: int = 0, limit: int = 10):
    return {"C++ — bu yuqori darajadagi, umumiy maqsadli dasturlash tili bo'lib, 1980-yillarda Bjarne Stroustrup tomonidan C tilini kengaytirish orqali ishlab chiqilgan. C++ dasturlash tili, asosan, samarali va yuqori tezlikda ishlaydigan dasturlarni yaratish uchun mo'ljallangan va ko'plab sohalarda keng qo'llaniladi, masalan, o'yinlar ishlab chiqish, tizim dasturlari, mobil ilovalar, robototexnika, sun'iy intellekt va boshqa sohalarda."}


@app.get("/c/")
def read_items(skip: int = 0, limit: int = 10):
    return {"C — bu past darajadagi, umumiy maqsadli dasturlash tili bo'lib, 1970-yillarda Dennis Ritchie tomonidan AT&T Bell Labs'da ishlab chiqilgan. C tili dasturlashning poydevori sifatida ko'plab zamonaviy dasturlash tillarining (masalan, C++, Java, Python) asosini tashkil etadi. C tili yuqori samaradorlik, tizim darajasida dasturlash imkoniyatlari va past darajadagi ishlov berish imkoniyatlari bilan mashhurdir."}


@app.get("/javascript/")
def read_items(skip: int = 0, limit: int = 10):
    return {"JavaScript — bu interaktiv va dinamik veb sahifalar yaratish uchun ishlatiladigan yuqori darajadagi dasturlash tili. JavaScript dasturlash tili, 1995-yilda Netscape kompaniyasidan Brendan Eich tomonidan yaratilgan va hozirda veb-ilovalar, server-side tizimlar va boshqa ko'plab sohalarda qo'llaniladi. JavaScript dasturlash tili, asosan, web sahifalarini interaktiv qilish va ularni dinamik tarzda boshqarish uchun ishlatiladi, lekin hozirda serverlar, mobil ilovalar va boshqa turli platformalarda ham ishlatiladi."}


@app.get("/css/")
def read_items(skip: int = 0, limit: int = 10):
    return {"CSS (Cascading Style Sheets) — bu veb sahifalarni bezash, ularning tashqi ko‘rinishini va tartibini boshqarish uchun ishlatiladigan stilizatsiya tilidir. CSS HTML yoki XML hujjatlariga formatlash qo‘llash uchun ishlatiladi, bu esa sahifalarni yanada chiroyli va foydalanuvchilar uchun qulay qilish imkonini beradi."}


@app.get("/php/")
def read_items(skip: int = 0, limit: int = 10):
    return {"PHP (Hypertext Preprocessor) — bu server tomonida ishlaydigan skriptlash tili bo‘lib, asosan dinamik veb sahifalar yaratish uchun ishlatiladi. PHP veb-serverda ishlaydi va foydalanuvchining so‘rovlariga javob sifatida HTML, CSS, JavaScript yoki boshqa ma'lumotlarni qaytaradi. PHP tili 1994-yilda Rasmus Lerdorf tomonidan ishlab chiqilgan va bugungi kunda eng mashhur server tomonidagi dasturlash tillaridan biri hisoblanadi."}


@app.get("/c#/")
def read_items(skip: int = 0, limit: int = 10):
    return {"C# dasturlash tili 1993–2001-yillarda Anders Xeylsberg va Skott Viltaumot boshchiligidagi Microsoft kompaniyasi muhandislar guruhi tomonidan Microsoft platformasi uchun ilovalarni dasturlash tili sifatida ishlab chiqilgan."}


@app.get("/go/")
def read_items(skip: int = 0, limit: int = 10):
    return {"2016-yil noyabr oyida Go va Go Mono shriftlari tip dizaynerlari Charlz Bigelow va Kris Xolms tomonidan maxsus Go loyihasi tomonidan foydalanish uchun chiqarildi. Go - bu Lucida Grande -ga o'xshash gumanistik sans-serif, Go Mono esa monofazoda. Ikkala shrift ham WGL4 belgilar to'plamiga mos keladi va katta x-balandligi va aniq harf shakllari bilan o'qilishi uchun mo'ljallangan. Go va Go Mono ikkalasi ham DIN 1450 standartiga mos keladi, ular qirrali nol, dumli kichik l va serifli katta I harfiga ega.[24][25]"}



