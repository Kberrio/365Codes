using UnityEngine;
using UnityEngine.UI;

public class GreetingManager : MonoBehaviour
{
    public InputField nameInputField;
    public Text greetingText;
    public Text inputPromptText;

    public void GreetUser()
    {
        string name = nameInputField.text.Trim();

        if (string.IsNullOrWhiteSpace(name))
        {
            greetingText.text = "You didn't enter a valid name.";
        }
        else
        {
            greetingText.text = $"Hello, {name}! Nice to meet you.";
        }
    }

    public void ClearInputField()
    {
        nameInputField.text = "";
        greetingText.text = "";
        inputPromptText.text = "Please enter your name:";
    }
}
