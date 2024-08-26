#include <QApplication>
#include <QMainWindow>
#include <QWebEngineView>
#include <QLineEdit>
#include <QVBoxLayout>
#include <QPushButton>

class SimpleBrowser : public QMainWindow {
public:
    SimpleBrowser(QWidget *parent = nullptr) : QMainWindow(parent) {
        // Create the web view
        webView = new QWebEngineView(this);

        // Create address bar
        addressBar = new QLineEdit(this);
        connect(addressBar, &QLineEdit::returnPressed, this, &SimpleBrowser::loadUrl);

        // Create back and forward buttons
        backButton = new QPushButton("Back", this);
        connect(backButton, &QPushButton::clicked, webView, &QWebEngineView::back);

        forwardButton = new QPushButton("Forward", this);
        connect(forwardButton, &QPushButton::clicked, webView, &QWebEngineView::forward);

        // Layout
        QVBoxLayout *layout = new QVBoxLayout;
        QHBoxLayout *navLayout = new QHBoxLayout;
        navLayout->addWidget(backButton);
        navLayout->addWidget(forwardButton);
        navLayout->addWidget(addressBar);
        layout->addLayout(navLayout);
        layout->addWidget(webView);

        QWidget *centralWidget = new QWidget(this);
        centralWidget->setLayout(layout);
        setCentralWidget(centralWidget);

        // Load a default page
        webView->load(QUrl("https://www.example.com"));
    }

private:
    QWebEngineView *webView;
    QLineEdit *addressBar;
    QPushButton *backButton;
    QPushButton *forwardButton;

    void loadUrl() {
        QString url = addressBar->text();
        if (!url.startsWith("http://") && !url.startsWith("https://")) {
            url = "http://" + url;
        }
        webView->load(QUrl(url));
    }
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    SimpleBrowser browser;
    browser.show();
    return app.exec();
}