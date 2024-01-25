import UIKit

class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let label = UILabel()
        label.text = "Hello, World!"
        label.textAlignment = .center
        label.frame = CGRect(x: 0, y: 0, width: 300, height: 100)
        label.center = view.center
        
        view.addSubview(label)
    }
}

import PlaygroundSupport
let viewController = ViewController()
PlaygroundPage.current.liveView = viewController
