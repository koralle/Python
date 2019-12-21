$$
memo[n][up_limit\_w] = \begin{cases}
  memo[n+1, uplimit\_w] (uplimit\_w < wv[n, 0]) \\
  max(memo[n+1, uplimit\_w], memo[n+1, uplimit\_w - wv[n, 0]] + wv[n, 1]) (Otherwise)
\end{cases}
$$