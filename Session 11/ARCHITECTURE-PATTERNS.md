# Architecture patterns

### What is architecture patterns <font size='1'>[read more](https://bit.ly/3cKrGZa)</font> 
***Abstract:** A general, reusable solution to a commonly occurring problem in software architecture.*

### Architecture pattern vs. design pattern
*Architectural patterns are similar to software design pattern but have a broader scope.*

### Types
1. [Layered pattern](#layered-pattern)
2. [Client-server pattern](#client-server-pattern)
3. [Master-slave pattern](#master-slave-pattern)
4. [Pipe-filter pattern](#pipe-filter-pattern)
5. [Broker pattern](#broker-pattern)
    and more...

___
#### Layered pattern
This pattern used in `structure programs`, can be decomposed into groups of subtasks, each layer provides services to the next layer.

<p align='center'><img src='https://bit.ly/3CWmSur' alt='Pic' width='150'/></p>

##### Common layers
* Presentation layer
* Application layer
* Business logic layer
* Data access layer

##### Usage
* Desktop applications
* E-commerce web applications
___

#### Client-server pattern
This pattern consists of `server and multiple clients`. Clients request services from the server, and the server provides relevant services to those clients. In other words, <u>the server continues to listen to client requests</u>.

<p align='center'><img src='https://bit.ly/3cHIhwD' alt='Pic' width='200'/></p>

##### Usage
* Online applications (email)

___

#### Master-slave pattern
This pattern consists of `master and slaves`. The master distributes the tasks among identical slave, and computes a final result from the results which the slaves return.

<p align='center'><img src='https://bit.ly/3AOBppe' alt='Pic' width='500'/></p>


##### Usage
* In database replication. <font size='2'>[read more](https://bit.ly/3BdufMY)</font> 
* Peripherals connected to a bus in a computer system. <font size='2'>[read more](https://bit.ly/3KHVxho)</font> 
___
#### Pipe-filter pattern 
This pattern used in `structure systems` which produces and processes a stream of data. Each processing step is enclosed within a `filter`. Data to be processed is passed through pipes. <font size='2' color='gray'>These pipes used in buffering or synchronization.</font> <font size='2'>[read more](https://bit.ly/3TI8iwo)</font>

<p align='center'><img src='https://bit.ly/3ehMx6w' alt='Pic' width='500'/></p>

##### Usage
* Compilers
* Workflows in bioinformatics
___
#### Broker pattern
This pattern used in `structure distributed systems` with decoupled components. These components can interact with each other by remote service invocations. **A broker (Connector)** component is responsible for the coordination of communication among components.

<p align='center'><img src='https://bit.ly/3B81WiO' alt='Pic' width='500'/></p>

##### Usage
* Message broker softwares <font size='2'>[read more](https://bit.ly/3BbhjH7)</font> 
  * [Apache ActiveMQ](https://activemq.apache.org/)
  * [Apache Kafka](https://kafka.apache.org/)
  * [RabbitMQ](https://www.rabbitmq.com/)
  * [JBoss Messaging](https://jbossmessaging.jboss.org/)
___
#### Resources
10 Common Software Architectural Patterns in a nutshell - medium - [link](https://bit.ly/3cHos8K)