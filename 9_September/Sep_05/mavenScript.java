// src/main/java/com/example/banking/model/Account.java
package com.example.banking.model;

import java.math.BigDecimal;
import java.util.UUID;

public class Account {
    private final UUID id;
    private final String ownerName;
    private BigDecimal balance;
    private final AccountType type;

    public Account(String ownerName, BigDecimal initialBalance, AccountType type) {
        this.id = UUID.randomUUID();
        this.ownerName = ownerName;
        this.balance = initialBalance;
        this.type = type;
    }

    // Getters and setters
    public UUID getId() { return id; }
    public String getOwnerName() { return ownerName; }
    public BigDecimal getBalance() { return balance; }
    public AccountType getType() { return type; }

    public void deposit(BigDecimal amount) {
        if (amount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Deposit amount must be positive");
        }
        balance = balance.add(amount);
    }

    public void withdraw(BigDecimal amount) throws InsufficientFundsException {
        if (amount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive");
        }
        if (balance.compareTo(amount) < 0) {
            throw new InsufficientFundsException("Insufficient funds for withdrawal");
        }
        balance = balance.subtract(amount);
    }
}

// src/main/java/com/example/banking/model/AccountType.java
package com.example.banking.model;

public enum AccountType {
    CHECKING,
    SAVINGS,
    MONEY_MARKET
}

// src/main/java/com/example/banking/exception/InsufficientFundsException.java
package com.example.banking.exception;

public class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String message) {
        super(message);
    }
}

// src/main/java/com/example/banking/service/BankingService.java
package com.example.banking.service;

import com.example.banking.model.Account;
import com.example.banking.exception.InsufficientFundsException;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.math.BigDecimal;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

public class BankingService {
    private static final Logger logger = LogManager.getLogger(BankingService.class);
    private final Map<UUID, Account> accounts = new HashMap<>();

    public Account createAccount(Account account) {
        accounts.put(account.getId(), account);
        logger.info("Created account: {}", account.getId());
        return account;
    }

    public Account getAccount(UUID id) {
        return accounts.get(id);
    }

    public void transfer(UUID fromId, UUID toId, BigDecimal amount) throws InsufficientFundsException {
        Account fromAccount = getAccount(fromId);
        Account toAccount = getAccount(toId);

        if (fromAccount == null || toAccount == null) {
            throw new IllegalArgumentException("Invalid account ID");
        }

        fromAccount.withdraw(amount);
        toAccount.deposit(amount);

        logger.info("Transferred {} from account {} to account {}", amount, fromId, toId);
    }
}

// src/main/java/com/example/banking/App.java
package com.example.banking;

import com.example.banking.model.Account;
import com.example.banking.model.AccountType;
import com.example.banking.service.BankingService;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.math.BigDecimal;

public class App {
    private static final Logger logger = LogManager.getLogger(App.class);

    public static void main(String[] args) {
        logger.info("Starting Banking Application");

        BankingService bankingService = new BankingService();

        Account account1 = new Account("John Doe", new BigDecimal("1000.00"), AccountType.CHECKING);
        Account account2 = new Account("Jane Doe", new BigDecimal("2000.00"), AccountType.SAVINGS);

        bankingService.createAccount(account1);
        bankingService.createAccount(account2);

        try {
            bankingService.transfer(account1.getId(), account2.getId(), new BigDecimal("500.00"));
            logger.info("Transfer successful");
        } catch (Exception e) {
            logger.error("Transfer failed: {}", e.getMessage());
        }

        logger.info("Banking Application Finished");
    }
}

// src/test/java/com/example/banking/service/BankingServiceTest.java
package com.example.banking.service;

import com.example.banking.model.Account;
import com.example.banking.model.AccountType;
import com.example.banking.exception.InsufficientFundsException;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import java.math.BigDecimal;

public class BankingServiceTest {
    private BankingService bankingService;
    private Account account1;
    private Account account2;

    @Before
    public void setUp() {
        bankingService = new BankingService();
        account1 = bankingService.createAccount(new Account("Test1", new BigDecimal("1000.00"), AccountType.CHECKING));
        account2 = bankingService.createAccount(new Account("Test2", new BigDecimal("2000.00"), AccountType.SAVINGS));
    }

    @Test
    public void testTransfer() throws InsufficientFundsException {
        bankingService.transfer(account1.getId(), account2.getId(), new BigDecimal("500.00"));
        assertEquals(new BigDecimal("500.00"), account1.getBalance());
        assertEquals(new BigDecimal("2500.00"), account2.getBalance());
    }

    @Test(expected = InsufficientFundsException.class)
    public void testTransferInsufficientFunds() throws InsufficientFundsException {
        bankingService.transfer(account1.getId(), account2.getId(), new BigDecimal("1500.00"));
    }

    @Test
    public void testGetAccount() {
        Account retrievedAccount = bankingService.getAccount(account1.getId());
        assertNotNull(retrievedAccount);
        assertEquals(account1.getId(), retrievedAccount.getId());
    }
}