## **Experiment Report Requirements: Measuring TLB Size**

### **1. Introduction**

* Briefly describe the purpose of the experiment: understanding Translation Lookaside Buffer (TLB) behavior and estimating TLB size through controlled memory-access patterns.
* Summarize the core idea behind the test program (e.g., varying stride sizes to reveal TLB misses).

### **2. Experimental Methodology**

* Provide a clear explanation of the testing strategy:

  * How the test program accesses memory (e.g., stride-based pointer chasing or array stepping).
  * How different strides correspond to different numbers of touched pages.
  * Why this helps identify TLB capacities and levels.
* Include hardware/environment descriptions:

  * CPU model
  * Cache hierarchy information
  * Page size
  * OS and compiler version
* Describe how measurements were collected (e.g., timing, performance counters if used).

### **3. Experimental Results**

* Present the results in readable tables or plots.

  * Access latency vs. number of pages or stride size.
* Clearly mark observed “jumps” or inflection points that suggest TLB boundaries.

### **4. Analysis**

* Interpret the results:

  * Estimate TLB size (entries).
  * Discuss whether multiple TLB levels can be inferred.
* Compare your findings with official hardware specifications (if available).
* Provide explanations for discrepancies or unexpected behaviors.

### **5. Conclusion**

* Summarize key findings.
* Reflect on what the experiment demonstrates about virtual memory, page translation, and TLB performance.

### **6. Appendix**

* Include the source code of the test program.
* Include raw measurement data.

