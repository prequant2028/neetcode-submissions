class Page:
    def __init__(self, url):
        self.url=url
        self.next=None
        self.prev=None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage=Page(homepage)
        self.curpage=self.homepage
        self.size=1
        self.curpagenum=1

    def visit(self, url: str) -> None:
        page=Page(url)
        self.curpage.next=page
        page.prev=self.curpage
        self.curpage=page

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curpage.prev:
                self.curpage=self.curpage.prev
            else:
                break
        return self.curpage.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curpage.next:
                self.curpage=self.curpage.next
            else:
                break
        return self.curpage.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)