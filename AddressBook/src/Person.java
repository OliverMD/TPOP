import java.util.List;

/**
 * Created by oliver on 17/02/15.
 */
public class Person implements Entry {

    private String firstName;
    private String lastName;

    private String number;

    private List<Watcher> watchers;

    public Person(String firstName, String lastName, String number) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.number = number;
    }

    @Override
    public String getLabel() {
        return this.firstName + " " + this.lastName;
    }

    /**
     * Registers a watcher so that
     */
    @Override
    public void register(Watcher watcher) {
        this.watchers.add(watcher);

    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
        this.watchers.forEach((watcher) -> {watcher.update();});
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }
}
