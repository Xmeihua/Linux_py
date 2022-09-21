一、Git的工作原理：


Workspace：工作区
Index/Stage：暂存区
Repository：仓库区
Remote：远程仓库
分布式版本控制系统，每个人的电脑都是一个完整的版本库


二、Git的主要操作：

Linux:
Cd + 路径：进入某个文件夹
Pwd: 显示当前文件路径
Ls -all：看到当前目录下的所有内容


提交到暂存取：
Git init: 把当前目录变成git可以管理的仓库
Git add + 文件名：把文件添加到暂存区
Git commit -m + 注释：告诉Git把文件提交到仓库
Git status：查看是否有文件未提交


版本回退：
Git diff + 文件名：查看文件的改动
Git log：显示从近到远的三次提交日志（git log -pretty=oneline可以使得显示的信息不那么复杂，只有版本号和commit时候的注释，我在Mac上操作需要:wp 退出log的模式）
Git Checkout + 文件名：用于add后还没commit之前
Git reset —hard HEAD^：退回上一个版本
Git reset —hard HEAD~100：退回到往回数第100个版本（如果有的话。。。）
Git reset —hard 版本号（从git log 或git reflow里获取）


撤销修改：
Git checkout — 文件名：丢弃工作区的修改


删除文件：
Git rm + 文件名/直接在工作区目录下删除文件
如果想撤销删除文件：git checkout —文件名


提交到Git远程仓库：
Git remote add origin + git仓库地址（从网页版复制粘贴然后添加.git即可）：将本地仓库和远程仓库关联
Git push -u origin master：把本地库的内容推送到远程仓库（第一次推送的时候添加-u参数，之后可以不添加）


克隆远程库的内容到本地：
Git alone git仓库地址


创建/合并分支：
Git checkout -b dev：创建并切换分支
Git branch：查看所有分支，当前分支会添加一个星号
Gti checkout dev：切换分支
Git merge dev：合并指定分支到当前分支上（git merge —no-ff -m “merge with no-ff” dev 合并dev分支，禁用fast-forward，不会丢失分支信息）
Git branch -d dev：删除dev分支


从远程库上更新代码：
Git pull：如果本地工作区上针对最新的远程库代码版本有更新，使用pull不会覆盖这个更新


三、工作区与暂存区的区别：
工作区：即在电脑上看到的目录（除了.git隐藏目录版本之外，我在Mac电脑上没有看到这个文件夹，但是之前使用Windows的时候是有的）
版本库：即.git，存了很多东西，最重要的即为版本库，还有Git自动创建的分支master，以及指向master的一个指针HEAD


四、远程仓库：
需要注册Github账号，然后在网页版上创建repository，这个新创建的仓库目前是空的，可以做的操作有：
关联一个本地的仓库，然后把本地仓库的内容推送到Git的仓库
从别的仓库引入代码


五、分支使用策略：
master应该是非常稳定的，一般情况下在dev上干活，需要线上发布，或者dev代码稳定后合并到master上来
修复bug的时候，每个bug都可以创建一个临时分支来修复，修复完成后合并分支，然后将临时分支删除
如果在dev上的工作还没有完成，又需要紧急修复另一个404bug：
可以使用git stash把当前工作现场隐藏起来（文件暂存）
解决完紧急bug之后切换回dev分支，使用git stash list查看暂存内容
Git stash apply/git stash pop, 后者恢复的同时会把stash的内容也删除了
