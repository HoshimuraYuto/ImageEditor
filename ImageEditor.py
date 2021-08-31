import os
import glob
import random
import string
import imghdr
import tkinter as tk
from tkinter import DoubleVar, filedialog, messagebox, ttk
import cv2
import piexif
import tkinterdnd2 as tkdnd2


root = tkdnd2.Tk()
root.title("ImageEditor")
root.geometry("320x320")
root.resizable(width=0, height=0)


def main():
  if not messagebox.askyesno('確認', '実行しますか?'): 
    return messagebox.showinfo("キャンセル", "キャンセルしました")
  path = path_box.get()
  files = glob.glob(path + "/*.*")
  progressBar.configure(maximum=len(files))
  for file in files:
    if imghdr.what(file) == None:
      continue
    if delExif_var.get():
      del_exif(file)
    if not imgSize_var.get() == "" and not int(imgSize_var.get()[0]) == 0:
      img_resize(file)
    img_quality(file)
    if randomRename_var.get():
      random_rename(path, file)

    progressBar_var.set(progressBar_var.get() + 1)
    progressBar.update()

  messagebox.showinfo("成功", "実行完了")
  progressBar_var.set(0)
  progressBar.update()



def drop(event):
  if os.path.isfile(event.data):
    messagebox.showerror("エラー", "ディレクトリを指定してください。")
  else:
    path_box_var.set(event.data)


def select_dir():
  idir = "/"
  file_path = filedialog.askdirectory(initialdir=idir)
  if len(path_box.get()) != 0:
    path_box.delete(0, tk.END)
  path_box.insert(tk.END, file_path)


def del_exif(file):
  if (imghdr.what(file) == "jpeg"):
    piexif.remove(file)


def img_resize(file):
  img = cv2.imread(file)
  img_height, img_width = img.shape[:2]
  if imgSize_WH_var.get() == "0":
    if img_width > int(imgSize_var.get()):
      w = int(imgSize_var.get())
      h = round(img_height * (w / img_width))
      cv2.imwrite(file, cv2.resize(img, dsize=(w, h)))
  else:
    if img_height > int(imgSize_var.get()):
      h = int(imgSize_var.get())
      w = round(img_width * (h / img_height))
      cv2.imwrite(file, cv2.resize(img, dsize=(w, h)))


def img_quality(file):
  cv2.imwrite(
      file,
      cv2.imread(file),
      [cv2.IMWRITE_JPEG_QUALITY, quality_scale.get()]
  )


def random_rename(path, file):
  os.rename(file, os.path.join(
      path,
      "".join(random.choices(string.ascii_letters, k=10)) +
      str(os.path.splitext(file)[1])
  )
  )


def round_scale(val):
  scale_var.set(round(int(float(val))))


def limit_entry(action, index, value_if_allowed,
                prior_value, text, validation_type, trigger_type, widget_name):
  if value_if_allowed.isdecimal():
    return True
  elif index == "0" and prior_value:
    return True
  else:
    return False


path_box_var = tk.StringVar()
path_box = tk.Entry(root, textvar=path_box_var, width=30)
path_box.place(x=20, y=20, width=280)
path_box.drop_target_register(tkdnd2.DND_FILES)
path_box.dnd_bind('<<Drop>>', drop)


ref_button = ttk.Button(text="フォルダ選択...", command=select_dir)
ref_button.place(x=20, y=55)


scale_var = DoubleVar()
scale_label = ttk.Label(text="圧縮レベル")
scale_label.place(x=20, y=110)
scale_label_var = ttk.Label(textvariable=scale_var)
scale_label_var.place(x=100, y=110)


quality_scale = ttk.Scale(
    length=200,
    from_=0,
    to=100,
    variable=scale_var,
    command=round_scale
)
quality_scale.set(60)
quality_scale.place(x=20, y=125, width=280)


imgSize_WH_var = tk.StringVar()
imgSize_var = tk.StringVar()

imgSize_WH_var.set(0)
imgSize_W_btn = ttk.Radiobutton(
    value=0,
    variable=imgSize_WH_var,
    text="横"
)
imgSize_W_btn.place(x=20, y=155)

imgSize_H_btn = ttk.Radiobutton(
    value=1,
    variable=imgSize_WH_var,
    text="縦"
)
imgSize_H_btn.place(x=60, y=155)    

vc = (root.register(limit_entry), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
imgSize_Entry = tk.Entry(
  root, 
  textvar=imgSize_var, 
  width=20,
  validate="key",
  validatecommand=(vc)
  )
imgSize_Entry.place(x=100, y=151)


randomRename_var = tk.BooleanVar()
randomRename_var.set(True)
randomRename = ttk.Checkbutton(
    text="ランダム画像名にする",
    variable=randomRename_var
)
randomRename.place(x=20, y=185)


delExif_var = tk.BooleanVar()
delExif_var.set(True)
delExif = ttk.Checkbutton(
    text="EXIF情報を削除する",
    variable=delExif_var
)
delExif.place(x=20, y=205)


pathChanger_button = ttk.Button(
    text="実行する",
    command=main
)
pathChanger_button.place(x=20, y=230)


progressBar_var = DoubleVar()
progressBar = ttk.Progressbar(
    maximum=100,
    variable=progressBar_var,
    length=280
)
progressBar.place(x=20, y=290)


root.mainloop()