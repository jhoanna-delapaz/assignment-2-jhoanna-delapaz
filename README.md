## Assignment 2: Simple Distributed Message-Passing Coding Exercise
***
### Code Output and Revisions
***
`Progress #1` **Attempting to run MPI**
<p> I first ran the starter code on Jupyter Notebook. However, nothing happened and there I learned that MPI cannot run properly on notebook cells and needed a separate python file. </p>
<img width="538" height="283" alt="image" src="https://github.com/user-attachments/assets/75210634-79fc-46ec-823b-a8388d0b19f8" />
<br>
<br>

`Progress #2` **Installing requirements and running MPI** 
<p> Afterwards, I installed MPI from the Microsoft website and used !pip in the command prompt. I also just used Jupyter as a place to run the results connected to the .py file I made using "!mpiexec". Here are the results of the starter code:</p>
<img width="506" height="147" alt="image" src="https://github.com/user-attachments/assets/d875f331-7414-4285-87c6-f51b44d44494" />
<br>
<br>

`Progress #3` **Code Changes** 
<p> This is the revised if statement: Instead of just sending a greeting message, each worker process now performs an actual task and sends a computed result (sum) to the master. </p>
<img width="705" height="318" alt="image" src="https://github.com/user-attachments/assets/07c1a59b-d202-4061-b847-129b43523fe2" />
<br>
<br>

<p> This is the revised else statement: In this revision, this section allows each process to perform its assigned task by generating a unique data chunk based on its rank and computing the sum of those numbers, then sending the results back to the master process. I also organized the output messages.</p>
<img width="621" height="392" alt="image" src="https://github.com/user-attachments/assets/eb72addc-503b-4b83-b1e4-c0bb8fe6c17f" />
<br>
<br>

`Progress #4` **Final Output** 

<img width="524" height="339" alt="image" src="https://github.com/user-attachments/assets/28e49c76-ddb1-4872-baad-1b864049cbb5" />

---
### Guide Questions (Discussion and Reflection)
***
1. Why is message passing required in distributed systems?
- From what I observed, processes in distributed systems run independently and do not share the same memory. A form of communication must be made to fix this issue, and that is where message passing comes in. By sending and receiving messages, data can be exchanged. Without message passing, the processes would not be able to share results or coordinate tasks.

2. What happens if one process fails?
- If one process fails, the rest of the processes waits indefinitely for the messages. As a result, the program crashes or freezes. In basic MPI systems, there is commonly no automated recovery, so the programs ends up being stopped.

3. How does this model differ from shared-memory programming?
- As I previously mentioned, this message-passing program runs indepedently and its only form of communication is via messages. The processes do not overlap since they only send and receive data. In shared-memory programming, multiple processes directly access the same memory space unlike message-passing. It may be capable of updating simultaneously and considered faster, but needs synchronization to prevent errors.
