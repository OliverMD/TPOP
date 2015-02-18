import java.util.function.Supplier;

/**
 * Created by oliver on 17/02/15.
 */
public interface Entry {
    public String getLabel();


    public void register(Watcher watcher); //Subscribe to changes
}
