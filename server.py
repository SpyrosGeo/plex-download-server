from typing import Optional
from os import listdir 
from os.path import isfile,join
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware



origins = ["*"]

mypath = '/home/thatguy/Downloads'
app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins =origins,allow_methods=["*"],allow_headers=["*"])
@app.get('/movies')
async def read_root():
    onlyFiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
    return {"files":onlyFiles}
@app.post('/search')
async def post_search(request:Request):
    return await request.json()