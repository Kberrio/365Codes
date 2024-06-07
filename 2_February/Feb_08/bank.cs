using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        List<Account> accounts = new List<Account>();

        while (true)
        {
            Console.WriteLine("\nBanking System Menu:");
            Console.WriteLine("1. Create Account");
            Console.WriteLine("2. Deposit Money");
            Console.WriteLine("3. Withdraw Money");
            Console.WriteLine("4. View Balance");
            Console.WriteLine("5. Exit");
            Console.Write("Enter your choice: ");

            int choice = Convert.ToInt32(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    Console.Write("Enter account holder name: ");
                    string name = Console.ReadLine();
                    Console.Write("Enter initial balance: ");
                    decimal initialBalance = Convert.ToDecimal(Console.ReadLine());
                    Account account = new Account(name, initialBalance);
                    accounts.Add(account);
                    Console.WriteLine("Account created successfully!");
                    break;

                case 2:
                    Console.Write("Enter account number: ");
                    int depositAccNumber = Convert.ToInt32(Console.ReadLine());
                    Console.Write("Enter amount to deposit: ");
                    decimal depositAmount = Convert.ToDecimal(Console.ReadLine());
                    DepositMoney(accounts, depositAccNumber, depositAmount);
                    break;

                case 3:
                    Console.Write("Enter account number: ");
                    int withdrawAccNumber = Convert.ToInt32(Console.ReadLine());
                    Console.Write("Enter amount to withdraw: ");
                    decimal withdrawAmount = Convert.ToDecimal(Console.ReadLine());
                    WithdrawMoney(accounts, withdrawAccNumber, withdrawAmount);
                    break;

                case 4:
                    Console.Write("Enter account number: ");
                    int viewBalanceAccNumber = Convert.ToInt32(Console.ReadLine());
                    ViewBalance(accounts, viewBalanceAccNumber);
                    break;

                case 5:
                    Console.WriteLine("Exiting the program...");
                    Environment.Exit(0);
                    break;

                default:
                    Console.WriteLine("Invalid choice. Please enter a number between 1 and 5.");
                    break;
            }
        }
    }

    static void DepositMoney(List<Account> accounts, int accNumber, decimal amount)
    {
        Account account = accounts.Find(acc => acc.AccountNumber == accNumber);
        if (account != null)
        {
            account.Deposit(amount);
            Console.WriteLine("Amount deposited successfully!");
        }
        else
        {
            Console.WriteLine("Account not found!");
        }
    }

    static void WithdrawMoney(List<Account> accounts, int accNumber, decimal amount)
    {
        Account account = accounts.Find(acc => acc.AccountNumber == accNumber);
        if (account != null)
        {
            if (account.Withdraw(amount))
            {
                Console.WriteLine("Amount withdrawn successfully!");
            }
            else
            {
                Console.WriteLine("Insufficient balance!");
            }
        }
        else
        {
            Console.WriteLine("Account not found!");
        }
    }

    static void ViewBalance(List<Account> accounts, int accNumber)
    {
        Account account = accounts.Find(acc => acc.AccountNumber == accNumber);
        if (account != null)
        {
            Console.WriteLine($"Account Number: {account.AccountNumber}, Name: {account.HolderName}, Balance: {account.Balance}");
        }
        else
        {
            Console.WriteLine("Account not found!");
        }
    }
}

class Account
{
    private static int nextAccountNumber = 1;

    public int AccountNumber { get; }
    public string HolderName { get; }
    public decimal Balance { get; private set; }

    public Account(string holderName, decimal initialBalance)
    {
        AccountNumber = nextAccountNumber++;
        HolderName = holderName;
        Balance = initialBalance;
    }

    public void Deposit(decimal amount)
    {
        Balance += amount;
    }

    public bool Withdraw(decimal amount)
    {
        if (Balance >= amount)
        {
            Balance -= amount;
            return true;
        }
        return false;
    }
}
