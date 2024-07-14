import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@SpringBootApplication
public class SimpleMvcApplication {

    public static void main(String[] args) {
        SpringApplication.run(SimpleMvcApplication.class, args);
    }
}

@Controller
class HelloController {

    @GetMapping("/")
    @ResponseBody
    public String hello() {
        return "Hello, Spring MVC!";
    }
}