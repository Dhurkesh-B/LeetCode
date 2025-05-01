import java.util.Arrays;
import java.util.TreeMap;

class Solution {
    
    public int maxTaskAssign(int[] tasks, int[] workers, int pills, int strength) {
        Arrays.sort(tasks);    // Sort tasks by difficulty (ascending)
        Arrays.sort(workers);  // Sort workers by strength (ascending)

        int left = 0;
        int right = Math.min(tasks.length, workers.length); // Maximum possible tasks

        // Binary search to find the maximum number of assignable tasks
        while (left < right) {
            int mid = (left + right + 1) / 2; // Try assigning 'mid' tasks
            if (canAssign(tasks, workers, pills, strength, mid)) {
                left = mid; // If 'mid' tasks can be assigned, try for more
            } else {
                right = mid - 1; // If 'mid' tasks cannot be assigned, try for fewer
            }
        }

        return left; // The maximum number of tasks that can be assigned
    }

    private boolean canAssign(int[] tasks, int[] workers, int pills, int strength, int count) {
        TreeMap<Integer, Integer> availableWorkers = new TreeMap<>();

        // Consider the 'count' strongest workers for assigning the 'count' hardest tasks
        for (int i = workers.length - count; i < workers.length; i++) {
            availableWorkers.put(workers[i], availableWorkers.getOrDefault(workers[i], 0) + 1);
        }

        int remainingPills = pills;

        // Try to assign the 'count' hardest tasks (from the end of the sorted tasks array)
        for (int i = count - 1; i >= 0; i--) {
            int currentTaskStrength = tasks[i];

            // Find the weakest worker capable of handling the current task without a pill
            Integer capableWorker = availableWorkers.ceilingKey(currentTaskStrength);

            if (capableWorker != null) {
                // Assign the task to this worker
                decrementCount(availableWorkers, capableWorker);
            } else {
                // If no worker is strong enough, try using a pill on the weakest available worker
                if (remainingPills > 0) {
                    Integer pillEligibleWorker = availableWorkers.ceilingKey(currentTaskStrength - strength);
                    if (pillEligibleWorker != null) {
                        decrementCount(availableWorkers, pillEligibleWorker);
                        remainingPills--;
                    } else {
                        // No worker can handle the task even with a pill
                        return false;
                    }
                } else {
                    // No pills left and no worker strong enough
                    return false;
                }
            }
        }

        // All 'count' tasks could be assigned
        return true;
    }

    private void decrementCount(TreeMap<Integer, Integer> map, int key) {
        int count = map.get(key);
        if (count == 1) {
            map.remove(key);
        } else {
            map.put(key, count - 1);
        }
    }
}
