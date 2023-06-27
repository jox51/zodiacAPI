from fastapi import FastAPI
from lunisolar import ChineseDate

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/getZodiac')
async def getZodiac(year, month, day):
    conv_year = int(year)
    conv_month = int(month)
    conv_day = int(day)

    entered_date = ChineseDate.from_gregorian(
        conv_year, conv_month, conv_day)
    return {"result": entered_date.zodiac}
