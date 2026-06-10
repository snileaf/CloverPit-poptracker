-- Synchronize separate visual toggle items with the progressive skeleton item
local function skeletonSync(code, value)
	local prog = Tracker:FindObjectForCode("progressiveskeleton")
	if not prog then return end

	local vis = {
		Tracker:FindObjectForCode("progressiveskeleton_stage1_item"),
		Tracker:FindObjectForCode("progressiveskeleton_stage2_item"),
		Tracker:FindObjectForCode("progressiveskeleton_stage3_item"),
		Tracker:FindObjectForCode("progressiveskeleton_stage4_item"),
		Tracker:FindObjectForCode("progressiveskeleton_stage5_item"),
	}

	for i=1,5 do if not vis[i] then return end end

	local active = prog.Active
	local stage = tonumber(prog.CurrentStage) or 0

	if not active or stage <= 0 then
		for i=1,5 do vis[i].Active = false end
		return
	end

	if stage > 5 then stage = 5 end
	for i=1,5 do vis[i].Active = (i <= stage) end
end

ScriptHost:AddWatchForCode("prog skeleton sync", "progressiveskeleton", skeletonSync)
