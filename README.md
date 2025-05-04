This code is the speed comparison of KV Caching on/off.
本代码是，KV Caching打开/关闭的速度对比。<br>

介绍<br>
KV Caching（键值缓存） 是在生成文本时缓存前面计算过的注意力键（Key）和值（Value），避免重复计算，从而加快推理速度。<br>

有了 KV Caching 怎么样？<br>
&nbsp;&nbsp;&nbsp;&nbsp;·第一次生成 token 时：<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 模型算出前面所有 token 的 K、V，并保存下来<br>
&nbsp;&nbsp;&nbsp;&nbsp;·第二个 token 开始：<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 只计算新 token 的 K 和 V<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 然后跟前面缓存的 老 K 和 V 合并一起用<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 直接进行注意力操作，省去了重复计算<br>

对比不使用 caching 的情况：<br>
    ·不加缓存：<br>
        - 每次都重新计算前面所有 K/V，开销是 O(n²)<br>
    ·加了缓存：<br>
        - 每次只算新的 token，前面的直接复用，开销降到 O(n)<br>
        - 生成越多 token，速度优势就越明显！<br>
