# import java.util.ArrayList;
# import java.util.List;
# import java.util.Scanner;
#
# public class Main {
#     public static void main(String[] args) {
#         Scanner scanner = new Scanner(System.in);
#         // 总钱数
#         int N = scanner.nextInt();
#         // 购买物品个数
#         int m = scanner.nextInt();
#         int[] f = new int[N + 1];
#         // 分组，goods[i][0]为主件，goods[i][1]为附件1，goods[i][2]为附件2
#         Good[][] goods1= new Good[60][4];
#
#         for (int i = 1; i <= m; i++) {
#             int v = scanner.nextInt();
#             int p = scanner.nextInt();
#             int q = scanner.nextInt();
#
#             Good t = new Good(v, v * p);
#             if (q == 0) {
#                 goods1[i][0] = t;
#             } else {
#                 if (goods1[q][1] == null) {
#                     goods1[q][1] = t;
#                 } else {
#                     goods1[q][2] = t;
#                 }
#             }
#         }
#
#         for (int i = 1; i <= m; i++) {
#             for (int j = N; j >= 0 && goods1[i][0] != null; j--) {
#                 //以下代码从分组中选择价值最大的。共五种情况：不选主件，选主件，选附件1和主件，选附件2和主件，选附件1和附件2和主件
#                 Good master = goods1[i][0];
#                 int max = f[j];
#                 if (j >= master.v && max < f[j - master.v] + master.vp) {
#                     max = f[j - master.v] + master.vp;
#                 }
#                 int vt;
#                 if (goods1[i][1] != null) {
#                     if (j >= (vt = master.v + goods1[i][1].v)
#                             && max <  f[j - vt] + master.vp + goods1[i][1].vp) {
#                         max = f[j - vt] + master.vp + goods1[i][1].vp;
#                     }
#                 }
#                 if (goods1[i][2] != null) {
#                     if (j >= (vt = master.v + goods1[i][1].v + goods1[i][2].v)
#                             && max < f[j - vt] + master.vp + goods1[i][1].vp + goods1[i][2].vp) {
#                         max = f[j - vt] + master.vp + goods1[i][1].vp + goods1[i][2].vp;
#                     }
#                 }
#                 f[j] = max;
#             }
#         }
#
#         System.out.println(f[N]);
#     }
# }
#
# class Good {
#     int v;
#     int vp;
#     public Good(int v, int vp) {
#         this.v = v;
#         this.vp = vp;
#     }
# }

while True:
    try:
        N, m = map(int, input().strip().split())
        a = [[0]*(N+1) for i in range(m+1)]
        goods = []
        for i in range(m):
            goods.append(list(map(int, input().strip().split())))
        for i in range(1, m+1):
            for j in range(1, N+1):
                if goods[i-1][2] == 0:   # 表示是主件
                    if goods[i-1][0]<=j:    # <=j表示买的起可以有选择, 这时候有两种选择，可以买也可以不买，选择最优的方案
                        a[i][j] = max(a[i-1][j], a[i-1][j - goods[i-1][0]]+goods[i-1][1]*goods[i-1][0])
                        # a[i][j] 表示用j元钱去买i件物品的最优解（这里就是（价格和重要性乘积）最大值）
                else:
                    if goods[i-1][0]+goods[goods[i-1][2]-1][0]<=j:   # 要买附件的话，必须先买主件，所以必须有能买两件的钱
                        a[i][j] = max(a[i-1][j],
                                      a[i-1][j - goods[i-1][0]]+goods[i-1][0]*goods[i-1][1],        # 这一行是根据  麦麦麦麦迪  的问题进行修改的 2019.3.20
                                      a[i-1][j-goods[i-1][0] - goods[goods[i-1][2]-1][0]]+goods[i-1][0]*goods[i-1][1]+goods[goods[i-1][2]-1][0]*goods[goods[i-1][2]-1][1])
        print(max([max(row) for row in a]))   # 这时候矩阵右下角并不是最大值，需要求整个矩阵的最大值
    except:
        break