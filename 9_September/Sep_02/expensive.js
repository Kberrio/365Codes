const calculatePrimes = (max) => {
    const primes = [];
    for (let i = 2; i <= max; i++) {
      let isPrime = true;
      for (let j = 2; j <= Math.sqrt(i); j++) {
        if (i % j === 0) {
          isPrime = false;
          break;
        }
      }
      if (isPrime) {
        primes.push(i);
      }
    }
    return primes;
  };
  
  const max = 10000000; // 10 million
  console.time('Prime calculation');
  const primes = calculatePrimes(max);
  console.timeEnd('Prime calculation');
  
  console.log(`Found ${primes.length} prime numbers up to ${max}`);
  console.log(`Last 10 primes found: ${primes.slice(-10).join(', ')}`);