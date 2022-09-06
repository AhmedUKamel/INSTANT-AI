# Design patterns

## What is design patterns
Is a general repeatable solution to a commonly occurring problem in software design.

> Design pattern is not a code. It is a description for how to solve a problem that can be used in many different situations.

## Types
### Creational design patterns
* [Singleton](#singleton)
* [Observer](#observer)
* [Factory](#factory)
* Builder, Prototype, Multiton and more...

### Structural design patterns
* [Decorator](#decorator)
* Adapter, Proxy, Composite, Bridge and more...

### Behavioral design patterns
* Blackboard, Command, Iterator, State and more...

#### Singleton
**Usage:** When an application needs one, and only one, instance of an object.
**Sample code:**

~~~java
public class Singleton {
    private static final Singleton INSTANCE;

    private Singleton() {}

    public static Singleton getInstance() {
        if(INSTANCE == null) {
            INSTANCE = new Singleton();
        }
        return SingletonHolder.INSTANCE;
    }
}
~~~

#### Observer
**Usage:** When an application needs distributed push-based notifications.
**Sample code:**

~~~java
public interface Observable {
    void update(String message);
}

public interface Subject {
    void addCourse(Observable observable);
    void delCourse(Observable observable);
    void notifyAllMembers();
}

public class Course implements Subject {
    private String name;
    private String availability;
    private List<Observable> observableList;
    
    public Course(String name) {
        this.name = name;
        observableList = new ArrayList<>();
    }

    @Override
    public void addCourse(Observable observable) {
        observableList.add(observable);
    }

    @Override
    public void delCourse(Observable observable) {
        observableList.remove(observable);
    }

    @Override
    public void notifyAllMembers() {
        for (Observable observer : observableList)
            observer.update(availability);
    }

    public void setAvailability(boolean available) {
        availability = this.name + (available ? " Available" : " Unavailable");
        notifyAllMembers();
    }
}

public class Student implements Observable {
    private String name;

    public Student(String name) {
        this.name = name;
    }

    @Override
    public void update(String message) {
        System.out.println(this.name + " has a new notification : " + message);
    }
}
~~~

#### Factory
**Usage:** When an application needs to standardize the architectural model for a range of results.
**Sample code:**
~~~java
public class Sandwich {
    private String name;
    private Double price;

    public void setName(String name) {
        this.name = name;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public void details() {
        System.out.println(name + " costs " + price + " $");
    }
}

public class CheeseBurger extends Sandwich {
    public CheeseBurger () {
        setName("Cheese Burger");
        setPrice(5.0);
    }
}

public class ChickenBurger extends Sandwich {
    public ChickenBurger () {
        setName("Chicken Burger");
        setPrice(7.4);
    }
}

public class SandwichFactory {
    public static final int CHEESE_BURGER = 1;
    public static final int CHICKEN_BURGER = 2;

    public static Sandwich prepareSandwich (int sandwichID) {
        if (sandwichID == CHEESE_BURGER)
            return new CheeseBurger();
        else if (sandwichID == CHICKEN_BURGER)
            return new ChickenBurger();
        else
            return null;
    }
}
~~~

#### Decorator
**Usage:** When application wants to add behavior or state to individual objects at run-time.
**Sample code:**
~~~java
public interface Sandwich {
    double getCost();
    String getDescription();
}

public class SandwichDecorator implements Sandwich {
    private Sandwich sandwich;

    public SandwichDecorator (Sandwich sandwich) {
        this.sandwich = sandwich;
    }

    @Override
    public double getCost () {
        return this.sandwich.getCost();
    }

    @Override
    public String getDescription () {
        return this.sandwich.getDescription();
    }
}

public class BasicSandwich implements Sandwich {
    @Override
    public double getCost() {
        return 10;
    }

    @Override
    public String getDescription() {
        return "Bread";
    }
}

public class Beef extends SandwichDecorator {
    public Beef(Sandwich sandwich) {
        super(sandwich);
    }

    @Override
    public double getCost() {
        return super.getCost() + 5;
    }

    @Override
    public String getDescription() {
        return super.getDescription() + ", Beef";
    }
}

public class Cheese extends SandwichDecorator {
    public Cheese(Sandwich sandwich) {
        super(sandwich);
    }

    @Override
    public double getCost() {
        return super.getCost() + 2;
    }

    @Override
    public String getDescription() {
        return super.getDescription() + ", Cheese";
    }
}
~~~
___
#### Resources
Software design pattern - Wikipedia - [link](https://en.wikipedia.org/wiki/Software_design_pattern)
Design Patterns - SourceMaking - [link](https://sourcemaking.com/design_patterns)
Software Design Pattern - Malik Abualzait - [link](https://www.youtube.com/playlist?list=PLZeX1aIDYSn8qNDPcqwyvOtGZkMQwPjCg)
