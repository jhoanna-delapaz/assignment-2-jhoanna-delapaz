from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # get the process rank
size = comm.Get_size()  # the total number of processes

if rank == 0:  # guessing rank 0 is the master process
    print("Master process gathering results...\n")

    for i in range(1, size):
        message = comm.recv(source=i)
        print(f"Received from process {i}:")
        print(f"  Task: Data Chunk {message['chunk']}")
        print(f"  Computed Sum: {message['result']}\n")

else:
    # Assigned task based on process rank
    # Each process has its data chunk (depending on the rank)
    data_chunk = list(range(rank * 10, rank * 10 + 10))

    # Simple computation: sum of numbers in the assigned task
    computed_sum = sum(data_chunk)

    # The output message includes:
    message = {
        "rank": rank,  # process rank
        "chunk": rank,  # assigned task (data chunk number)
        "result": computed_sum # computed result (sum)
    }

    # Send computed result to master process (rank 0)
    comm.send(message, dest=0)


