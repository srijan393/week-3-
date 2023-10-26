import sys
def get_platform():
    platform = sys.platform
    return platform
if __name__ == "__main__":
    platform = get_platform()
    print(f"Operating System Platform: {platform}")