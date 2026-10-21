from PIL import Image,ImageDraw,ImageFont
from fastapi import FastAPI,File,UploadFile,Response
import io
import os
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # 测试用，生产别 *
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/upload')
async def upload(file:UploadFile = File(...)):
    data = await file.read()

    with Image.open(io.BytesIO(data)) as img:
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), 'mai sakurajima', fill=(255, 0, 0), font=ImageFont.load_default())

        # 处理后的图写进内存
        buf = io.BytesIO()
        fmt = img.format or 'PNG'          # 保留原格式，没有就 PNG
        if fmt == 'JPEG' and img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        img.save(buf, format=fmt)
        buf.seek(0)                         # 指针复位到开头，否则读到空
        content = buf.getvalue()

    media_type = 'image/jpeg' if fmt == 'JPEG' else f'image/{fmt.lower()}'
    out_name = 'watermarked_' + file.filename

    return Response(
        content=content,
        media_type=media_type,
        headers={
            # inline: 浏览器直接显示；attachment: 触发下载
            "Content-Disposition": f'inline; filename="{out_name}"'
        }
    )