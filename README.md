# My-Gpt
هوش مصنوعی محلی با استفاده از Ollama و رابط کاربری (UI)
# **LocalAI-WebUI**

## **معرفی پروژه**

LocalAI-WebUI یک رابط کاربری تحت وب ساده، کاربرپسند و قدرتمند برای مدیریت و تعامل با مدل‌های هوش مصنوعی محلی است. این پروژه با استفاده از **Ollama** به کاربران امکان می‌دهد مدل‌های زبانی بزرگ (LLMs) را به‌صورت محلی اجرا کرده و بدون نیاز به اتصال به اینترنت یا APIهای خارجی از آن‌ها بهره ببرند.

این ابزار برای **توسعه‌دهندگان، محققان و علاقه‌مندان به هوش مصنوعی** طراحی شده است تا به راحتی از قابلیت‌های مدل‌های هوش مصنوعی در محیط محلی استفاده کنند. همچنین، از **نمایش صحیح متون فارسی (RTL) و انگلیسی (LTR)** پشتیبانی می‌کند و امکان مقایسه همزمان خروجی چندین مدل را فراهم می‌آورد.

---

## **ویژگی‌های کلیدی**

### **۱. مدیریت مدل‌های محلی با Ollama**
✅ نصب و مدیریت آسان مدل‌های مختلف هوش مصنوعی.  
✅ **حفظ حریم خصوصی:** تمامی پردازش‌ها به‌صورت محلی انجام می‌شود و نیازی به ارسال داده‌ها به سرورهای خارجی نیست.  

### **۲. رابط کاربری (UI)**
✅ رابط کاربری **واکنش‌گرا، ساده و کاربرپسند**.  
✅ **پشتیبانی از زبان‌های مختلف**، از جمله فارسی و انگلیسی.  
✅ نمایش صحیح متون **RTL (فارسی) و LTR (انگلیسی)**.  
✅ **حالت تیره (Dark Mode)** برای تجربه کاربری بهتر.  

### **۳. مقایسه مدل‌ها**
✅ امکان **مقایسه خروجی چندین مدل** به‌صورت همزمان.  
✅ ارزیابی عملکرد مدل‌ها در وظایفی مانند **ترجمه، خلاصه‌سازی و تولید متن**.  

### **۴. پاسخ‌های استریم بلادرنگ**
✅ دریافت پاسخ‌ها به‌صورت **بلادرنگ و استریم شده**.  

### **۵. مدیریت خطا و بازیابی**
✅ تشخیص و مدیریت خطاهای مختلف، از جمله **مشکلات اتصال، انتخاب مدل‌های نامعتبر، Timeout و خطاهای API**.  

### **۶. تاریخچه جستجو**
✅ ذخیره و بازیابی **تاریخچه پرسش‌ها و پاسخ‌ها**.  

### **۷. قابلیت سفارشی‌سازی**
✅ **شخصی‌سازی رابط کاربری** بر اساس نیازهای خاص کاربران.  
✅ امکان **اضافه کردن ویژگی‌های جدید** مانند تحلیل عملکرد مدل‌ها یا ابزارهای تجسم داده.  

### **۸. طراحی سازگار با دسکتاپ**
✅ **بهینه‌شده برای استفاده در دستگاه‌های دسکتاپ**.  

---

## **موارد استفاده**

🔹 **تحقیق و توسعه**: تست و ارزیابی مدل‌های مختلف برای اهداف تحقیقاتی.  
🔹 **پروژه‌های چندزبانه**: پردازش متون فارسی و انگلیسی.  
🔹 **آموزش**: یادگیری و آموزش مدل‌های هوش مصنوعی.  
🔹 **توسعه نرم‌افزار**: استفاده از مدل‌های محلی برای ایجاد نرم‌افزارهای هوش مصنوعی بدون نیاز به سرورهای خارجی.  
🔹 **تولید محتوا**: تولید مقالات، ترجمه متون و سایر موارد.  

---

## **پیش‌نیازها**

برای نصب و استفاده از **LocalAI-WebUI**، به موارد زیر نیاز دارید:  

1. **Python** نسخه **۳.۸ یا بالاتر** ➝ [دانلود](https://www.python.org/downloads/)  
2. **Visual Studio Code** ➝ [دانلود](https://code.visualstudio.com/Download)  
3. **Ollama** (آخرین ورژن) ➝ [دانلود](https://ollama.com/download)  
4. **مدل‌های مورد نیاز در مثل  Ollama**:  
   - `qwen2.5:1.5b`  
   - `deepseek-r2:1.5b`  

---

## **مراحل نصب و راه‌اندازی**

### **۱. نصب Ollama**
🔹 به [سایت Ollama](https://ollama.com/download) مراجعه کرده و نسخه مناسب برای سیستم عامل خود را دانلود و نصب کنید.  

### **۲. نصب Python**
🔹 آخرین نسخه **Python** را از [اینجا](https://www.python.org/downloads/) دانلود و نصب کنید.  

### **۳. نصب Visual Studio Code**
🔹 ویرایشگر کد **VS Code** را از [اینجا](https://code.visualstudio.com/Download) دانلود و نصب کنید.  

### **۴. انتخاب و نصب مدل‌های مورد نیاز**
🔹 به [صفحه مدل‌های Ollama](https://ollama.com/models) مراجعه کنید و مدل‌های **`qwen2.5:1.5b`** و **`deepseek-r2:1.5b`** را دانلود و نصب کنید.  

### **۵. اجرای پروژه**
1. فایل زیپ پروژه را **از حالت فشرده خارج کنید**.  
2. پوشه پروژه را در **Visual Studio Code** باز کنید.  
3. فایل **`app.py`** را اجرا کنید.  

### **۶. استفاده از رابط کاربری**
🔹 در فیلد مربوطه **پرامپت خود را وارد کنید**.  
🔹 مدل‌های مورد نظر را از لیست انتخاب کنید.  
🔹 دکمه **Enter** را فشار دهید و منتظر پاسخ باشید.  

---

## **مدیریت خطاها**

این برنامه شامل مدیریت جامع خطا برای موارد زیر است:
- **مشکلات اتصال به Ollama**.  
- **انتخاب مدل‌های نامعتبر**.  
- **سناریوهای Timeout**.  
- **خطاهای عمومی API**.  
- **خطاهای اتصال**.  

---

## **جمع‌بندی**

**LocalAI-WebUI** یک ابزار قدرتمند، کاربرپسند و کاربردی برای تعامل با **مدل‌های هوش مصنوعی محلی** است. این پروژه امکان **مدیریت، مقایسه و شخصی‌سازی مدل‌ها** را فراهم می‌کند و به‌ویژه برای کاربران **فارسی‌زبان و پروژه‌های چندزبانه** مناسب است.  

### **🎉 تبریک! شما موفق شدید!**



