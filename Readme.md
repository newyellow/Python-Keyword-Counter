使用方法：

	Step 1:

		用 sublime 編輯 keywordSetting 檔案，輸入想要尋找的關鍵字
		（換行分隔每個關鍵字）

		可以為關鍵字分類，在文字後面加上數字即可
		目前可以分類成 0 ~ 9 總共十種分類
		詳情請參考 keywordSetting 裡的範例


	Step 2:

		把文章存檔放到 SourceArticles 裡面
		如果文章原先是存在 word 或 excel，需要複製貼上到 sublime 存成純文字檔案


	Step 3:

		用 sublime 打開 Python Script 裡面的 main.py
		然後按下 command + B （執行程式）
		當底下出現「計算完成！」就ＯＫ了


	Step 4:

		撈取的結果會存成 csv 檔，放在 Results 資料夾內
		並會取名成和文章一樣的名稱
		可以使用 Apple 的 Numbers 這套軟體打開
		（Excel 會因為編碼不符合，中文字會變成亂碼）
