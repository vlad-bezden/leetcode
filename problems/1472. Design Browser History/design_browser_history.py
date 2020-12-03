from collections import deque


class BrowserHistory:
    def __init__(self, homepage: str) -> None:
        self.history = deque()
        self.history.append(homepage)
        self.index = 0

    def visit(self, url: str) -> None:
        while len(self.history) > self.index + 1:
            self.history.pop()
        self.history.append(url)
        self.index += 1

    def back(self, steps: int) -> str:
        self.index = max(self.index - steps, 0)
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        self.index = min(len(self.history) - 1, self.index + steps)
        return self.history[self.index]


if __name__ == "__main__":
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")
    browserHistory.visit("facebook.com")
    browserHistory.visit("youtube.com")
    assert browserHistory.back(1) == "facebook.com"
    assert browserHistory.back(1) == "google.com"
    assert browserHistory.forward(1) == "facebook.com"
    browserHistory.visit("linkedin.com")
    assert browserHistory.forward(2) == "linkedin.com"
    assert browserHistory.back(2) == "google.com"
    assert browserHistory.back(7) == "leetcode.com"

    print("PASSED!!!")
