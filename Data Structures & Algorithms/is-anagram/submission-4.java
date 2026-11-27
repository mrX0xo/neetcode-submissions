class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> dump = new HashMap<>();
        Boolean ans = false;

        for (char charS : s.toCharArray()){
            if (dump.containsKey(charS)){
                dump.put(charS, dump.getOrDefault(charS, 0) + 1);
            }else{
                dump.put(charS, 1);
            }
        }

        for (char charT : t.toCharArray()){
            if (dump.containsKey(charT)){
                dump.put(charT, dump.getOrDefault(charT, 0) - 1);
            }else{
                dump.put(charT, 1);
            }
        }

        for (Integer i : dump.values()){
            if (i == 0){
                ans = true;
            }else{
                return false;
            }
        }

        return ans;


        
    }
}
