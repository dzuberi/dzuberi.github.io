---
title: OS Projects
date: 2023-04-20
tags: [Operating Systems, C, C++, Linux, IPC, RPC, gRPC]
---

I took Graduate Intro to Operating Systems through the OMSCS at Georgia Tech and learned a lot! The class was basically just 3 projects plus some exams. The projects were learning experiences.

I would like to share the code and reports, but I think that these same projects are completed by current students.

# Project 1 

The first project was to implement a file transfer protocol using `tcp` sockets. This involved familiarizing myself with the linux sockets API and handling many different kinds of errors.

Part two was to enhance the above implementation to be able to use multiple threads. We used a `steque` with mutex locks and conditionals.

# Project 3 

The second project was to imlpement a proxy server using libcurl. The server takes in a base URL as an argument which serves as the address to fetch files from and receives requests from a download client.

Part two was a cache server, which consisted of two parts. The first is the proxy server, which sends requests to the cache using IPC and then receives data using shared memory IPC. The second is the cache which receives requests from the server, checks if the file is cached, and then sends the data using shared memory IPC to the server. For this part, I designed and implemented my own protocol for the two to talk to each other using Message Queues and designed a custom struct to share data using shared memory IPC.

# Project 4 

Project 4 was to use gRPC with protobuf3 to implement some file operations: Store, Fetch, List, Stat, and Delete.

Part 2 was to implement a distributed filesystem using gRPC and protobuf3. It used an inotify watcher thread and an additional asynchronous RPC request for the server state from the client.
