from script1 import perform_ping_scan
from PIL import Image

def main():
    target_ip = input("Enter the target IP address or range: ")
    results = perform_ping_scan(target_ip)

    print("\nScan results:")
    for host, status in results:
        print(f"Host: {host} is {status}")

if __name__ == "__main__":
    main()
    
# Open a JPG file from the repository
jpg_file_path = "c:/Users/anders/TestGit/TestGit/12.jpg"
img = Image.open(jpg_file_path)
img.show()