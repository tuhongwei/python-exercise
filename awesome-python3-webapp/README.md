## 安装依赖包
pip3 install -r requirements.txt

## 如果要在本地项目中安装依赖包
python3 -m venv .
source bin/activate

## 执行mysqly语句
mysql -u root -p < www/schema.sql