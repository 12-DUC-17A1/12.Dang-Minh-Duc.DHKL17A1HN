import requests

def get_posts_from_api():
    url = 'https://jsonplaceholder.typicode.com/posts'
    
    try:
        # Gửi yêu cầu GET đến API
        response = requests.get(url)
        # Kiểm tra xem yêu cầu có thành công không
        if response.status_code == 200:
            posts = response.json()  # Chuyển đổi kết quả thành JSON
            return posts
        else:
            print("Không thể lấy dữ liệu từ API. Mã trạng thái:", response.status_code)
            return []
    except Exception as e:
        print("Có lỗi xảy ra:", e)
        return []

def display_posts(posts):
    # Hiển thị tổng số bài post
    print(f"Tổng số bài post: {len(posts)}")
    # Hiển thị danh sách các bài post
    for post in posts:
        print(f"UserID: {post['userId']}, ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 50)

if __name__ == "__main__":
    # Lấy danh sách các bài post từ API
    posts = get_posts_from_api()
    # Hiển thị danh sách các bài post
    display_posts(posts)