import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SyslogParser {

    private static final Pattern SYSLOG_PATTERN = Pattern.compile(
            "<(\\d+)>(\\w{3}\\s+\\d+\\s+\\d+:\\d+:\\d+)\\s+(\\S+)\\s+(\\S+):\\s+(.*)");

    public static void main(String[] args) {
        String fileName = "syslog.txt";
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                parseSyslogMessage(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void parseSyslogMessage(String syslogMessage) {
        Matcher matcher = SYSLOG_PATTERN.matcher(syslogMessage);
        if (matcher.matches()) {
            int priority = Integer.parseInt(matcher.group(1));
            String timestamp = matcher.group(2);
            String host = matcher.group(3);
            String tag = matcher.group(4);
            String message = matcher.group(5);

            int facility = priority / 8;
            int severity = priority % 8;

            System.out.println("Timestamp: " + timestamp);
            System.out.println("Host: " + host);
            System.out.println("Facility: " + facility);
            System.out.println("Severity: " + severity);
            System.out.println("Tag: " + tag);
            System.out.println("Message: " + message);
            System.out.println("----------------------------------------");
        } else {
            System.err.println("Invalid Syslog message format: " + syslogMessage);
        }
    }
}
