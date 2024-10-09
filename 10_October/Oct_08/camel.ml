(* Alpha-Beta pruning in OCaml *)

(* Define a type for representing game states *)
type game_state = int list  (* Simplified, can represent anything *)

(* Define a type for player, MAX and MIN represent two players *)
type player = MAX | MIN

(* Define the opposite player *)
let opponent = function
  | MAX -> MIN
  | MIN -> MAX

(* Terminal test function, checks if a game state is terminal (e.g., win/loss/draw) *)
let is_terminal (gs : game_state) : bool =
  gs = [] || List.fold_left max 0 gs = 0  (* Simplified, replace with actual game logic *)

(* Evaluation function, evaluates a given game state for MAX player *)
let evaluate (gs : game_state) : int =
  List.fold_left (+) 0 gs  (* Simplified, replace with actual heuristic evaluation *)

(* Function to generate the next possible game states *)
let next_states (gs : game_state) : game_state list =
  List.map (fun _ -> List.map (fun x -> if x > 0 then x - 1 else 0) gs) gs  (* Simplified *)

(* Alpha-Beta pruning algorithm *)
let rec alpha_beta player state alpha beta depth =
  if is_terminal state || depth = 0 then
    evaluate state  (* Return the evaluation of the terminal state *)
  else if player = MAX then
    maximize state alpha beta depth
  else
    minimize state alpha beta depth

(* Maximizing function for MAX player *)
and maximize state alpha beta depth =
  let rec go a = function
    | [] -> a  (* No more moves *)
    | s::ss ->
      let score = alpha_beta MIN s a beta (depth - 1) in
      let new_alpha = max a score in
      if new_alpha >= beta then new_alpha
      else go new_alpha ss
  in go alpha (next_states state)

(* Minimizing function for MIN player *)
and minimize state alpha beta depth =
  let rec go b = function
    | [] -> b  (* No more moves *)
    | s::ss ->
      let score = alpha_beta MAX s alpha b (depth - 1) in
      let new_beta = min b score in
      if new_beta <= alpha then new_beta
      else go new_beta ss
  in go beta (next_states state)

(* Function to find the best move for MAX player *)
let best_move state =
  List.fold_left (fun acc s -> if alpha_beta MIN s min_int max_int 3 > alpha_beta MIN acc min_int max_int 3 then s else acc)
                 (List.hd (next_states state))
                 (next_states state)

(* Example usage *)
let () =
  let initial_state = [3; 5; 7] in  (* Simplified game state *)
  let depth = 3 in
  Printf.printf "Best move: %s\n" (String.concat " " (List.map string_of_int (best_move initial_state)))
