title: "Crypto: BitCoin"
date: 2015-04-16 18:00:00
tags:
---

回归技术，从技术的视角重新审视一下数字货币。从这个角度看，中文网页上95%以上的信息都是垃圾信息，真正介绍相关知识的网页信息真的不多。

起点当然是比特币。这是我的学习思路，也顺便晒出来，也许有点分享价值。这个系列，不是导引或教程，而是学习笔记。


###Step1

读中本聪的论文[《Bitcoin: A Peer-to-Peer Electronic Cash System》](https://bitcoin.org/bitcoin.pdf)或者它的[翻译版](http://www.8btc.com/wiki/bitcoin-a-peer-to-peer-electronic-cash-system)。

中本聪在论文中明确提出，基于IP地址的投票机制可能被操控，所以是不可靠的，而基于工作量机制的方式，则能体现出更大程度上的民主，每个CPU一票，只要大多数人不是脑残的，那么，系统就能稳定可靠。但显卡、矿机打破了这个理想，POW已经与中本聪否定的IP投票机制没有本质区别了。


###Step2

了解ECDSA（The Elliptic Curve Digital Signature Algorithm）椭圆曲线签名算法，ECDSA协议框架和DSA基本一致，只不过ECDSA使用的椭圆函数域，而DSA使用普通乘法域Zp。DSA中所使用模p下的乘法运算对应ECDSA的椭圆函数域下的加法运算。可以参考[这个链接](http://zhiqiang.org/blog/it/das-and-ecdsa-rsa.html)，该博主细致的介绍了DSA，但对于ECDSA，博主将链接引向了[这篇论文](http://cs.ucsb.edu/~koc/ccs130h/notes/ecdsa-cert.pdf)。

这是一个庞大的领域，DSA涉及到数论，然后是椭圆曲线、抽象代数。即使以实用目的不去追踪那些基础原理而仅仅去读那篇概述论文，也要涉及到有限域。有限域是域的子集，域是环的一种，环是一种阿贝尔群。群是代数中最普遍的结构之一，也本应该是数学中的常识之一。我们真的是一群文盲罢了。先把手头的这两件事做好，然后有空暇时间了，真的该从头学一下这些数学常识。

最终决定放弃对ECDSA的理解，太难了，没有学过对应的数学基础，也没有足够的时间。只跳过ECDSA，其他的都要按部就班的进行。但是，ECDSA是比特币系统的基石，不懂这个算法，就不可能真的理解该系统。所以，只是把对该算法的理解放到最后，先学那些外围的东西，最后再理解该算法。


###Step3
[How the Bitcoin protocol actually works](http://www.michaelnielsen.org/ddi/how-the-bitcoin-protocol-actually-works/)这篇文章不错，通过自行设计了demo系统，循序渐进的对该原型进行完善，逐步引入了比特币系统的要素概念，对于没有了解过比特币系统的人，这是一个很好的起点，对于了解了基本概念的人，也能重新温习一下这些设计要素被引入的原因。数字货币是一个新兴的领域，目前还远远不够成熟，甚至幼稚。基于POW的技术机制去制衡利益冲动，这正是其幼稚的体现。利益的冲动只能依靠利益机制去约束，所以，POS是一个更有价值的方向，虽然目前的POS机制也存在各种类型的问题和缺陷。

Prof of Work解决的是资格确认的问题---谁有资格对交易进行确认？答案是，那些掌握算力的人有这个资格。但随着算力的专业化集中，这就改变了问题的性质，有算力的人变成了“权威机构“，只有他们有资格。这跟银行的权威是殊途同归的，有算力的那些矿池，跟作者提及的发序列号的银行，其实就有了相同的本质。

作者引入这些要素的次序是这样的：digital signing --->  Serial number ---> public serial number bank ---> majority verify  ---> prof of work

但这仍然不完整，POW是一个有严重缺陷的机制：

prof of work ---> prof of stock ---> margin verify

该文的作者谈完demo之后，接着谈及比特币系统中的transaction数据格式和block的数据格式。作者使用[blockexplorer](http://blockexplorer.com)提供的信息对block和tx进行解读。比如，一个block的[例子](http://blockexplorer.com/rawblock/0000000000000060bc4cb270085928b9abd44a80701d36e467d3dd30a6059c3f)：[初始transaction](http://blockexplorer.com/rawtx/5c81f8f4486410cc839b13b9e5c4b25442073d3a8e2a6839d90f4496f73b2d2f) [转帐transaction](http://blockexplorer.com/rawtx/72d7e1cc1de53b6da91c32cb05224779004a03bbbcfb45170e27006aa06aed2c)。与用户的视角不同，bitcoin的基础数据结构是transaction，而不是wallet address，从技术实现的层面看，wallet address并没有什么特殊的意义，整个体系的代码都是围绕着transaction和block这两种数据结构而构建。wallet address可能是wallet客户端所关注的，在某种程度上，可以看作这是transaction和blockchain的一种view。而对于系统的运行而言，address的意义仅限于余额检查，所以它更像是对transaction处理代码施加的一种约束条件。在原文中，作者有这么一句话：in Bitcoin there’s not really any separate, persistent “coins” at all, just a long series of transactions in the block chain. It’s a clever idea to realize that you don’t need persistent coins, and can just get by with a ledger of transactions.所谓的“币”，这其实是不存在的，实际上所谓的“币”只是transactions的一个假象，比特币的本质是由transactions构成的blockchain，这就是比特币。

blockchain在本质上是一个分布式的公共数据库。bitcoin代码其实是一个简陋的数据库操作系统DBMS。这个DBMS的设计其实比较粗陋和原始，它还有足够的完善余地和改进空间，在数据的存储、处理效率、安全性等等方面，目前的bitcoin只是一个起点，它还远远不够成熟，所以在目前，数字货币系统仍然属于投机品的范畴，如果将其作为价值储藏的方式，恐怕还太过激进。数字货币社区对于中本聪的溢美之词显然过了，有人将中本聪称为隐世大师，甚至有人将他视为帮助地球人的外星人或认为他来自于未来。比特币系统只是因为发生在金融层面，所以被很多人重视，它的实用价值、社会价值可能很高，但技术角度看，甚至未必会超高hadoop。也可以认为，比特币系统开创了一种新的数据组织方式，这是一种新型的数据库系统需求。但毫无疑问，它是DBMS的一个分支。


###Step4

[Mastering Bitcoin: Unlocking Digital Cryptocurrencies](http://www.amazon.com/Mastering-Bitcoin-Unlocking-Digital-Cryptocurrencies/dp/1449374042)

截止到此刻(2015年1月10日)，关于数字货币的技术书籍大约只有三五本。这是其中的一本，也是相对最完整全面的一本。读完上述文章之后，就可以考虑读这本书了，kindle版大约13美元，不贵。

Bitcoin was not simply a digital currency, but a network of trust that could also provide the basis for so much more than just currencies....It was the most exciting technology I had encountered since the Internet. --前言

There are no physical coins or event digital coins per se. The coins are implied in transactions that transfer value from sender to recipient. Users of bitcoin own keys that allow them to prove ownership of transactions in the bitcoin network, unlocking the value to spend it and transfer it to new recipient.

The private key is completely independent of the bitcoin protocol and can be generated and managed by the user's wallet software without reference to the blockchain or access to the Internet。私钥完全独立于比特币协议，私钥的产生不依赖于比特币网络。The bitcoin private key is just a number.  You can pick your private keys randomly using just a coin, pencil, and paper: toss a coin 256 times and you have the binary digits of a random private key you can use in a bitcoin wallet. The public key can then be generated from the private key.  私钥可以使用扔硬币256次的方式产生。The private key can be any number between 1 and n-1, where n is a constant( n= 1.158 * 10^77, slightly less than 2^256) defined as the order of the elliptic curve used in bitcoin. 私钥是一个介于1到2^256-1之间的任意随机数。Bitcoin software uses the underlying operating system's random number generator's to produce 256 bit entropy randomness. For the truly paranoid, nothing beats dice, pencil, and paper. 比特币客户端使用系统的随机数发生器产生256位的随机数，但严格来讲，最安全的方式仍然是用骰子。第四章。

生成一个随机数私钥之后，用Elliptic curve multiplication运算得到公钥，对公钥进行Hash运算，得到钱包地址。这两步操作均为单向操作，基于计算复杂度的不可逆。

UTXO: 比特币系统中并没有任何形式的“币“，有的，仅仅是UTXO，即unspend transaction output，UTXO从一个账户解锁，然后由另一个帐号控制，每次转移的过程中，一般会发生UTXO的分裂，所以，系统中的UTXO会越来越多，最终可能是每聪就是一个UTXO。比特币系统追踪着所有的UTXO，而所有UTXO中的总金额，即为当前比特币系统中的总现金量。这是一个伟大而神奇的创造。这即为transaction链的牛逼之处。

从本质上看，UTXO才是该系统的核心。其实这就是一个分布式数据库。由此构成了一种开放式资产或开放式金融。但是，个人感觉，transaction技术+blockchain技术造成了大量的数据冗余，似乎并没有必要。既然是一个分布式数据库，可以进一步优化，让它回归数据库的实质，裁剪冗余，压缩数据量。个人断言，目前的比特币也好，二代币也好，都只是开放式资产的第一代技术，这才仅仅是一个开始，transaction和blockchain远远不是终点。


###以下是尚未使用到的资料


以下文章都还不错：

[比特币基本概念](http://www.8btc.com/wiki/bitcoin-basic-concepts)

[比特币技术进阶](http://www.8btc.com/wiki/bitcoin-technical-principles)

[Bitcoin的基本原理](http://blog.codingnow.com/2011/05/bitcoin.html)

[bitcoin的技术原理](http://zhiqiang.org/blog/it/technical-document-of-bitcoin.html)

[bitcoin的技术缺陷](http://zhiqiang.org/blog/finance/techinical-and-financial-deficit-of-bitcoin.html)

[Bitcoin源码分析-深入浅出剖析比特币](http://ar.newsmth.net/thread-1215b8fbbb78df6.html)

[bitcoin wiki](https://en.bitcoin.it/wiki/Main_Page)



当然，如果真的想弄懂，官方维基和源代码是必备的。

[github代码库](https://github.com/bitcoin/bitcoin)

[开发者文档](https://bitcoin.org/en/developer-documentation)

[wiki tech page](https://en.bitcoin.it/wiki/Category:Technical)

[相关论文](https://en.bitcoin.it/wiki/Research)

[developer guide](https://bitcoin.org/en/developer-guide)

[developer reference](https://bitcoin.org/en/developer-reference)

[developer example](https://bitcoin.org/en/developer-examples)

[block](https://en.bitcoin.it/wiki/Block)

[Transactions](https://en.bitcoin.it/wiki/Transactions)

[Contracts](https://en.bitcoin.it/wiki/Contracts)

[Smart property](https://en.bitcoin.it/wiki/Smart_Property)

[Protocol specification](https://en.bitcoin.it/wiki/Protocol_specification)

[Protocol rules](https://en.bitcoin.it/wiki/Protocol_rules)

[Get block template](https://en.bitcoin.it/wiki/Getblocktemplate)

[wallet protocol](https://en.bitcoin.it/wiki/Wallet_protocol)

[Script](https://en.bitcoin.it/wiki/Script)

[Scalability](https://en.bitcoin.it/wiki/Scalability)

[bitcoinj documentation](https://bitcoinj.github.io/#documentation)
[BIP](https://en.bitcoin.it/wiki/Bitcoin_Improvement_Proposal)


###书籍


[Bitcoin Internals: A Technical Guide to Bitcoin](http://www.amazon.com/Bitcoin-Internals-Technical-Guide-ebook/dp/B00DG8EPT0/)

[Bitcoin Programming](http://www.amazon.com/gp/product/1500176826)

[The Book Of Satoshi: The Collected Writings of Bitcoin Creator Satoshi Nakamoto](http://www.amazon.com/gp/product/1500176826)

[Great Chain of Numbers: A Guide to Smart Contracts, Smart Property and Trustless Asset Management](http://www.amazon.com/Great-Chain-Numbers-Contracts-Management-ebook/dp/B00IRUBMXO)

[Anonymous Cryptocurrencies: The rise of bitcoin alternatives that offer true anonymity](http://www.amazon.com/Cryptocurrencies-bitcoin-alternatives-offer-anonymity-ebook/dp/B00KZ6WANE)


[山寨币一览表](http://coinmarketcap.com/currencies/views/all/)

[山寨资产一览表](http://coinmarketcap.com/assets/views/all/)

摘抄的几个碎片概念：

Hash哈希（或译作“散列”）是一种函数，它把任何数字或者字符串输入转化成一个固定长度的输出。通过输出我们不可能反向推得输入，除非尝试了所有的可能的输入值。下面是一个简单的哈希函数的例子，平方根：17202的平方根是很容易求得的，它大概是131.15639519291463，所以一个简单的哈希函数的输出可能是输入的数字的平方根的后面几位小数，在这个例子里面就是9291463。但是，只给出9291463的话，我们几乎不可能推算出它是哪个输入的输出。现代加密哈希比如像SHA-256，比上面这个例子要复杂的多也要安全的多。哈希这个词也用于指代这样一个函数的输出值。
