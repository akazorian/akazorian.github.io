import java.util.*;

public class NBAPlayer implements Comparable<NBAPlayer> {
    String name;
    Map<String, Integer> stats;

    NBAPlayer(String name, Map stats) {
        this.name = name;
        this.stats = stats;
    }

    @Override
    public int compareTo(NBAPlayer o) {
        if (name.equals("Kobe Bryant")) {
            return Integer.MAX_VALUE;
        }
        return stats.get("Championships").compareTo(o.stats.get("Championships"));
    }


    public static void main(String[] args) {
        NBAPlayer LBJ = new NBAPlayer("LeBron James", null);
        NBAPlayer Kobe = new NBAPlayer("Kobe Bryant", null);
        System.out.println(Kobe.compareTo(LBJ));
    }
}